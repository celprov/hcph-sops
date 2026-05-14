# HCPH Analysis Notebooks

This section provides a set of Jupyter notebooks for in-depth analysis of the HCPH dataset.

## Getting Started

To run the notebooks interactively, you will first need to download the required datasets. We **strongly recommend using [DataLad](https://www.datalad.org/)**.

### Required Data

1. **Functional Connectivity (FC) Matrices:**  
   [https://github.com/TheAxonLab/hcph-fc](https://github.com/TheAxonLab/hcph-fc)
5. **Structural Connectivity (SC) Matrices:**  
   [https://github.com/TheAxonLab/hcph-sc](https://github.com/TheAxonLab/hcph-sc)
2. **fMRIPrep Derivatives (Generalization Sessions):**  
   [https://github.com/TheAxonLab/hcph-fmriprep-generalization](https://github.com/TheAxonLab/hcph-fmriprep-generalization)
3. **fMRIPrep Derivatives (Reliability Sessions):**  
   [https://github.com/TheAxonLab/hcph-fmriprep](https://github.com/TheAxonLab/hcph-fmriprep)
4. **HCPH Raw Dataset:**  
   [https://github.com/TheAxonLab/hcph-dataset](https://github.com/TheAxonLab/hcph-dataset)
   It is a heavy dataset, which is why we highly recommend using DataLad to get in memory only the few files needed.
   Depending on the analyses, you might only need the behavioral and phenotype table [mood_env_quest.tsv](https://github.com/TheAxonLab/hcph-dataset/blob/master/phenotype/mood_env_quest.tsv).
7. **MRIQC-generated Image Quality Metrics:**  
   [https://github.com/TheAxonLab/hcph-mriqc/group_*.tsv](https://github.com/TheAxonLab/hcph-mriqc/)

---

## Notebook Overview

Below is a brief summary of each notebook and the main analyses performed:

