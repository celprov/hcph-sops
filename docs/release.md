# Defacing
The first step before releasing the data is to deface the T1w and T2w images for all sessions.
To perform defacing, we are using a software called PyDeface (Gulban et al. 2019).
To proceed, run the following command in the command line:
```bash
    bash ./code/defacing/run_pydeface.sh
```

## Release checklist

1. **Verify defacing results**
   - Open a subset of T1w and T2w images with your preferred viewer (e.g., *FSLeyes*).
   - Confirm that all facial features were removed while brain tissue remains intact.
2. **Run quality checks**
   - Execute *MRIQC* on all sessions as described in [the MRIQC guidelines](data-management/mriqc.md).
   - Inspect individual and group reports, addressing any issues before continuing.
3. **Package and version the dataset**
   - Save new files with *DataLad*:
     ```shell
     datalad save -r -m "add: session <session_id>" sub-001/ses-<session_id>
     ```
   - Tag the dataset with a new version number:
     ```shell
     git tag -a "vX.Y.Z" -m "HCPh release X.Y.Z"
     ```
4. **Upload the release**
   - Push data and tags to the remotes:
     ```shell
     datalad push --to ria-storage
     datalad push --to origin
     git push origin --tags
     ```
   - Publish the new version on GitHub and upload the dataset to the designated repository (e.g., OSF or Zenodo).
5. **Update documentation**
   - Record the release in [changes.md](changes.md).

# References
[1]: Gulban, Omer Faruk, Dylan Nielson, Russ Poldrack, John Lee, Chris Gorgolewski, Vanessa Sochat, and Satrajit Ghosh. 2019. “Poldracklab/Pydeface: V2.0.0.” Zenodo. doi: 10.5281/zenodo.3524401.
