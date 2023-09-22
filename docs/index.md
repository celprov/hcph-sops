# The Human Connectome PHantom (HCPh) study: Standard Operating Procedures

| ![](assets/images/cohort1.png) |
|:--:|
| ***Figure 1. Experimental design of Cohort I.*** *The first section of the study involves acquiring 72 sessions across three scanners of a single subject.* |

## Summary

Unveiling how the brain's structure defines its distributed function and modulates the dynamics of processing holds the promise of triggering a revolution in neuroscience and applications to mental health and neurodegenerative diseases.
Magnetic resonance imaging (MRI) has proven a valuable, non-invasive way of probing both the architecture and activity of the brain in-vivo, with sufficient spatial and temporal resolution to understand many aspects of its function.
Although a large body of literature has shown strong correlations between structural and functional networks at the larger scales<sup>[1],[2],[3],[4]</sup>, the accumulated unreliability of MRI measurements from the scanner and through further steps of the research workflow impedes the link between structure, function, and dynamics at clinically relevant spatial and temporal scales.
In particular, the measurements obtained with MRI are highly indirect, spatiotemporally uncertain, and confounded by other sources of MR signal.
This complexity provides an immense informatics challenge that crosses multiple imaging modalities, including structural, functional, and dynamic connectivity approaches to understanding the human brain.
Nonetheless, functional and structural networks extracted from MRI have proven sufficient levels of reliability to discriminate between individuals<sup>[4],[5],[6],[7]</sup>, and such reliability has proven stable from months to years<sup>[8]</sup>.
Therefore, it is critical to characterize the reliability of this network’s phenotyping before these analytical approaches may be applied clinically<sup>[9],[10]</sup>.
In this project, we will first optimize the research workflow of MR network analyses to maximize the reliability of functional and structural connectivity matrices (so-called connectomes).
Indeed, these matrices have been shown to contain large ratios of false positives and false negatives in both the functional [11] and the structural<sup>[12],[13]</sup> cases.
 We hypothesize that such improvements in sensitivity and specificity of functional and structural networks generalize across scanners and subjects, allowing the univocal identification of individuals from their brain’s networks ("fingerprinting").
In order to be able to statistically separate and characterize the sources of signal variation, the project involves acquiring large amounts of repeated data on a small number of individuals.
This approach has recently been dubbed "precision MRI"<sup>[14]</sup> and focuses on individual differences rather than group differences.
The data acquisition approach is structured in three efforts with varying numbers of subjects, repetitions, and scanning devices.
The first two, called "Cohort I" and "Cohort II" are sequential in time, and collected on three different devices.
Cohort I involves a single individual who will undergo a total of 60 scanning sessions.
Subsequently, Cohort II involves six (6) individuals and a total of twelve (12) sessions each.
Finally, "Cohort III" is a quality control set involving 18 individuals and a total of two sessions each in a single scanner.
In total, the project plans for repeated MRI acquisition on 25 healthy, adult human subjects, across three different 3.0 Tesla (T) MRI scanners available at CHUV.
In addition to the new data, the project will reuse existing, open-access data to pilot various aspects of the MRI processing and analysis workflow to further support the overall reliability of the findings.

## Impact

Overall, this project will equip researchers with a framework for the extraction of reliable and precise structural, functional and dynamic networks that permit their joint modeling and analysis with interpretable and reproducible methods.
The project will publicly release two highly valuable datasets necessary for the improvement of the workflow for structural and functional network extraction under open access and reuse terms.
Upon conclusion, this study will mark a turning point for MRI research as a fundamental resource for academic training and a necessary assessment to unlock clinical applications in the long-term with the improvement of the reliability of MRI-network analyses.
At a local scale, the project will substantially contribute to ensuring the reliability of the MRI clinical workflow that routinely aids medical decisions at CHUV.

## Pre-registration

The experiments and hypotheses associated to the collection of Cohorts I and II will be pre-registered to further guarantee research rigor and seek early scrutiny and feedback from experts in the field, thereby generating consensus on data collection and analysis.
Researchers increasingly perceive pre-registration as a tool to maximize research transparency, improve study planning, and eliminate incentives conducive to dubious practices in the search for positive outcomes.
By pre-registering the study, we will maximize the impact and usefulness of this work.
A report on the Cohort I collection is undergoing pre-registration.
Similarly, a report on Cohort II will be similarly submitted to suitable journal or organization (such as the Peer Community in Registered Reports, PCIRR) for peer-review.
Additional reports and public communications of results of this project will be pre-registered whenever that is possible.


[1]: https://doi.org/10.1016/j.jneumeth.2010.01.014 "P. Hagmann et al., MR connectomics: Principles and challenges., J. Neurosci. Methods, vol. 194, no. 1, pp. 34–45, Jan. 2010, doi: 10.1016/j.jneumeth.2010.01.014."

[2]: https://doi.org/10.1073/pnas.0811168106 "C. J. Honey et al., *Predicting human resting-state functional connectivity from structural connectivity.*, Proc. Natl. Acad. Sci. U. S. A., vol. 106, no. 6, pp. 2035–40, Feb. 2009, doi:10.1073/pnas.0811168106."

[3]: https://doi.org/10.1073/pnas.1219562110 "A. M. Hermundstad et al., *Structural foundations of resting-state and task-based functional connectivity in the human brain*, Proc. Natl. Acad. Sci., vol. 110, no. 15, pp. 6169–6174, Apr. 2013, doi:10.1073/pnas.1219562110."

[4]: https://doi.org/10.1038/s41467-018-04614-w "G. Rosenthal et al., *Mapping higher-order relations between brain structure and function with embedded vector representations of connectomes*, Nat. Comm., vol. 9, no. 1, p. 2178, Jun. 2018, doi:10.1038/s41467-018-04614-w."

[5]: https://doi.org/10.1371/journal.pbio.0060159 "P. Hagmann et al., *Mapping the structural core of human cerebral cortex.*, PLoS Biol., vol. 6, no. 7, p. e159, Jul. 2008, doi:10.1371/journal.pbio.0060159."

[6]: https://doi.org/10.1038/nn.4135 "E. S. Finn et al., *Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity*, Nat. Neurosci., vol. 18, no. 11, pp. 1664–1671, Nov. 2015, doi:10.1038/nn.4135."

[7]: https://doi.org/10.1038/s41598-018-25089-1 "E. Amico and J. Goñi, *The quest for identifiability in human functional connectomes*, Sci. Rep., vol. 8, no. 1, p. 8254, May 2018, doi:10.1038/s41598-018-25089-1."

[8]: https://doi.org/10.1016/j.neuroimage.2019.02.002 "C. Horien, X. Shen, D. Scheinost, and R. T. Constable, *The individual functional connectome is unique and stable over months to years*, NeuroImage, vol. 189, pp. 676–687, Apr. 2019, doi:10.1016/j.neuroimage.2019.02.002."

[9]: https://doi.org/10.1038/s41562-019-0655-x "X.-N. Zuo, T. Xu, and M. P. Milham, *Harnessing reliability for neuroscience research*, Nat. Hum. Behav., vol. 3, no. 8, Art. no. 8, Aug. 2019, doi:10.1038/s41562-019-0655-x."

[10]: https://doi.org/10.1001/jamapsychiatry.2020.4272 "M. P. Milham, J. Vogelstein, and T. Xu, *Removing the Reliability Bottleneck in Functional Magnetic Resonance Imaging Research to Achieve Clinical Utility*, JAMA Psychiatry, vol. 78, no. 6, pp. 587–588, Jun. 2021, doi:10.1001/jamapsychiatry.2020.4272."

[11]: https://doi.org/10.1016/j.neuroimage.2011.10.018 "J. D. Power, K. A. Barnes, A. Z. Snyder, B. L. Schlaggar, and S. E. Petersen, *Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion*, NeuroImage, vol. 59, no. 3, pp. 2142–2154, Feb. 2012, doi:10.1016/j.neuroimage.2011.10.018."

[12]: https://doi.org/10.1016/j.neuroimage.2016.06.035 "A. Zalesky, A. Fornito, L. Cocchi, L. L. Gollo, M. P. van den Heuvel, and M. Breakspear, *Connectome sensitivity or specificity: which is more important?*, NeuroImage, vol. 142, pp. 407–420, Nov. 2016, doi:10.1016/j.neuroimage.2016.06.035."

[13]: https://doi.org/10.1038/s41467-017-01285-x "K. H. Maier-Hein et al., *The challenge of mapping the human connectome based on diffusion tractography*, Nat. Comm., vol. 8, no. 1, p. 1349, Nov. 2017, doi:10.1038/s41467-017-01285-x."

[14]: https://doi.org/10.1016/j.neuron.2017.07.011 "E. M. Gordon et al., *Precision Functional Mapping of Individual Human Brains*, Neuron, vol. 95, no. 4, pp. 791-807.e7, Aug. 2017, doi:10.1016/j.neuron.2017.07.011."
