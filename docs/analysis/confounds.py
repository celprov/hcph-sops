def get_confounds(dataset_path="/data/datasets/hcph-dataset"):
    import pandas as pd
    from pathlib import Path

    dataset_path = Path(dataset_path)

    # Read the scans.tsv file
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
