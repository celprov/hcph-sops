import pandas as pd
from pathlib import Path

def get_confounds_scanstsv(dataset_path="/data/datasets/hcph-dataset"):
    """
    Extract and process confound information from a `scans.tsv` file.

    This function reads a `scans.tsv` file from the specified dataset path, processes
    its contents to extract relevant confound information, and returns a DataFrame
    with additional metadata columns.

    Parameters:
    -----------
    dataset_path : str, optional
        The path to the dataset directory containing the `scans.tsv` file.
        Default is "/data/datasets/hcph-dataset".

    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame containing the processed confound information with the following columns:
        - `filename`: The original filename of the scan.
        - `acq_time`: The acquisition time of the scan.
        - `subject`: The subject identifier extracted from the filename.
        - `session`: The session identifier extracted from the filename.
        - `modality`: The modality of the scan (e.g., anat, func) extracted from the filename.
        - `task`: The task identifier extracted from the filename.
        - `pe_dir`: The phase encoding direction extracted from the filename.
        - `day_of_week`: The day of the week extracted from the acquisition time.
        - `time_of_day`: The rounded time of day extracted from the acquisition time.
    """

    ## Read the scans.tsv file
    dataset_path = Path(dataset_path)
    confounds_df = pd.read_csv(dataset_path / "scans.tsv", sep="\t")
    confounds_df.drop(columns=["randstr"], inplace=True)

    # Extract entities
    # Each echo and magnitude and phase part of each functional scans are recorded on separate line,
    # but we have only one final image so keep only one of the identical acq_time
    confounds_df = confounds_df.drop_duplicates(subset=["acq_time"])
    confounds_df = confounds_df.assign(
        subject=confounds_df["filename"].str.extract(r"sub-(\d+)/"),
        session=confounds_df["filename"].str.extract(r"ses-(\w+)/"),
        modality=confounds_df["filename"].str.split("/").str[2],
        task=confounds_df["filename"].str.extract(r"task-(\w+)_"),
        pe_dir=confounds_df["filename"].str.extract(r"dir-(\w+)_"),
    )

    # From the acq_time column, extract the day of week and time of day
    confounds_df = confounds_df.assign(
        datetime=pd.to_datetime(confounds_df["acq_time"])
    )
    confounds_df = confounds_df.assign(
        day_of_week=confounds_df["datetime"].dt.day_name(),
        time_of_day=confounds_df["datetime"].dt.round("H").dt.time,
    )
    confounds_df.drop(columns=["datetime"], inplace=True)

    return confounds_df


def get_iqms(iqms_path="/data/derivatives/hcph-mriqc/group_dwi.tsv", iqm_of_interest=["fd_mean"]):
    """
    Extract imaging quality metrics (IQMs) from a specified TSV file.
    This function reads a TSV file containing IQMs, extracts relevant metadata 
    (subject, session, modality, and task) from the `bids_name` column, and filters 
    the data to include only the specified IQMs of interest.
    Parameters:
    -----------
    iqms_path : str, optional
        Path to the TSV file containing the IQMs. Default is 
        "/data/derivatives/hcph-mriqc/group_dwi.tsv".
    iqm_of_interest : list of str, optional
        List of column names corresponding to the IQMs to retain in the output. 
        Default is ["fd_mean"].
    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame containing the extracted metadata (subject, session, 
        modality, task) and the specified IQMs of interest.
    """

    iqms_df = pd.read_csv(iqms_path, sep="\t")
    iqms_df = iqms_df.assign(
        subject=iqms_df["bids_name"].str.extract(r"sub-(\d+)_"),
        session=iqms_df["bids_name"].str.extract(r"ses-(\w+)_"),
        modality=iqms_df["bids_name"].str.split("_").str[-1],
        task=iqms_df["bids_name"].str.extract(r"task-(\w+)_"),
    )
    # Keep only the IQMs of interest
    iqms_df = iqms_df[["subject", "session", "modality", "task"] + iqm_of_interest]

    return iqms_df


def get_confounds(dataset_path="/data/datasets/hcph-dataset", iqms_path=None, iqm_of_interest=["fd_mean"]):
    """
    Extract and merge confounds from various sources for a given dataset.
    This function retrieves confounds from a dataset, optionally merges them with 
    image quality metrics (IQMs) if provided, and includes additional confounds 
    found in GitHub issue logs.
    Parameters:
        dataset_path (str): 
            Path to the dataset directory. Defaults to "/data/datasets/hcph-dataset".
        iqms_path (str, optional): 
            Path to the file containing IQMs. If provided, the IQMs will be merged 
            with the confounds DataFrame. Defaults to None.
        iqm_of_interest (list of str): 
            List of IQMs to extract from the IQMs file. Defaults to ["fd_mean"].
    Returns:
        pandas.DataFrame: 
            A DataFrame containing the merged confounds from the dataset, IQMs 
            (if provided), and mood-related confounds.
    """

    confounds_df = get_confounds_scanstsv(dataset_path)

    ## If iqms_path is provided, read the IQMs and merge them with the confounds
    if iqms_path:
        iqms_df = get_iqms(iqms_path, iqm_of_interest)

        # Merge the fd_mean values into the confounds DataFrame
        confounds_df = pd.merge(
            confounds_df, iqms_df, on=["subject", "session", "modality", "task"], how="left"
        )

    return confounds_df