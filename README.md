# Benchmarking of Publicly Available Shotgun Metagenomic Mock Communities

## Overview
This project is a part of ...

## File Structure and Descriptions
### Expected Pipelines
This folder structure contains subdirectories for each pipeline assessed. These are:
    
- **Amos**: Amos, G. C. A. et al. Developing standards for the microbiome field. Microbiome 8, 98, 10.1186/s40168-020-00856-3
(2020).

- **BMock12**: Sevim, V. et al. Shotgun metagenome data of a defined mock community using Oxford Nanopore, PacBio and Illumina
technologies. Sci Data 6, 285 (2019).

- **CamiSim**: Fritz, A., Lesker, T., Bremges, A. & McHardy, A. Cami 2 - multisample benchmark dataset of human microbiome project,
10.4126/FRL01-006425518 (2019).

- **NIST**: [SRA HERE]

- **Tourlousse**: Tourlousse, D. M. et al. Characterization and demonstration of mock communities as control reagents for accurate
human microbiome community measurements. Microbiol. Spectr. 10, e01915–21, 10.1128/spectrum.01915-21 (2022).
https://journals.asm.org/doi/pdf/10.1128/spectrum.01915-21.

Within each subdirectory are CSVs of ground truth standardized names and expected abundances. The annotated files have TAXIDs attached in the following format: **Species, RA, TAXID**.

### Pipelines
This folder contains the cleaned outputs from the raw pipeline output, as well as the statistics. The folder layout is identical to the **Expected Pipelines**, but there are subdirectories for each pipeline. Also, there is a [threshold]\_all\_stats\_replicates\_[genus/species].csv file, which summarizes the statistics for the community across all of the pipelines.

### Python_Src
This folder contains much of the project's code to convert raw data into data that can be analyzed. There are several subdirectories here. Omitted subdirectories were not needed for this project.

- `nist_confusion`: contains the code for making the confusion matrix tables in the supplement.
- `pipeline_clean`: contains all the pipeline cleaning code for bioBakery, JAMS, WGSA2, and Woltka.

- `compositions.py`: Aitchison Distance functions with associated test file.

- `figures_utils`: useful figure file functions.

### Utils
Contains many of the analysis tools to calculate statistics and tables for the manuscript.

- `analysis`: contains functions for statistical analysis.
    - `ad_vs_reads`: calculates the correlation between AD and read length.
    - `results`: folder for output of analysis
    - `summary_tables`: CSV summary table creation (AD, Sens, FPRA, Num_FP).
    - `analyze_stats.ipynb`: performs the majority of the combined statistical analysis, including KW test and combining the stats together into the `results/all_stats_species.csv` files. 

- `ncbi`: NCBI standardization and lineage searching protocols.
    - `names`: contains the name standardization functions
    - `lineage.py/.ipynb`: determines the correct genus name from TAXID.
    - `jams_convert.py`: annotates non-Excel JAMS output.
    - `species_annotated_to_genus`: converts all of the species-level annotated RA tables to genus-level.

- `paper`: diagrams and figures for the manuscript.
    - `heatmaps.ipynb`: creates the RA table comparison heatmaps.
    - `read_stats.ipynb`: creates and analyzes read stats tables

- `time`: calculates the time performance of each pipeline.

- `data_paths.py`: holds the path to the raw data on the Biowulf computing cluster. 