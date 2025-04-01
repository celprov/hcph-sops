def get_confounds(dataset_path="/data/datasets/hcph-dataset", iqms_path=None):
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

    # If iqms_path is provided, read the IQMs and merge them with the confounds
    if iqms_path:
        iqms_df = pd.read_csv(iqms_path, sep="\t")
        iqms_df = iqms_df.assign(
            subject=iqms_df["bids_name"].str.extract(r"sub-(\d+)_"),
            session=iqms_df["bids_name"].str.extract(r"ses-(\w+)_"),
        )
        iqms_df = iqms_df[["subject", "session", "fd_mean"]]

        # Merge the fd_mean values into the confounds DataFrame
        confounds_df = pd.merge(
            confounds_df, iqms_df, on=["subject", "session"], how="inner"
        )
        # Verify that the correct fd_mean has been associated with sessions
        assert (
            iqms_df.loc[iqms_df["session"] == "001", "fd_mean"].values[0]
            == confounds_df.loc[confounds_df["session"] == "001", "fd_mean"].values[0]
        ), f"FD mean pairing with confounds failed"
        assert (
            iqms_df.loc[iqms_df["session"] == "pilot20103060", "fd_mean"].values[0]
            == confounds_df.loc[
                confounds_df["session"] == "pilot20103060", "fd_mean"
            ].values[0]
        ), f"FD mean pairing with confounds failed"
        assert (
            iqms_df.loc[iqms_df["session"] == "pilot020", "fd_mean"].values[0]
            == confounds_df.loc[
                confounds_df["session"] == "pilot020", "fd_mean"
            ].values[0]
        ), f"FD mean pairing with confounds failed"

    return confounds_df
