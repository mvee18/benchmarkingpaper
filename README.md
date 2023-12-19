# Benchmarking of Publicly Available Shotgun Metagenomic Mock Communities

## Overview
This repository is the main analysis for the associated shotgun metagenomics benchmarking manuscript. It contains the raw data, analysis methods, and documentation.

## File Structure and Descriptions

- `figures.ipynb`: main file for analysis and generation of statistics. 

- `requirements.txt`: a list of packages needed for this analysis. You can install these by first creating a Python virtual environment, then:

        pip install -r requirements.txt



### Expected Pipelines
This folder structure contains subdirectories for each pipeline assessed. These are:
    
- **Amos**: Amos, G. C. A. et al. Developing standards for the microbiome field. Microbiome 8, 98, 10.1186/s40168-020-00856-3
(2020).

- **BMock12**: Sevim, V. et al. Shotgun metagenome data of a defined mock community using Oxford Nanopore, PacBio and Illumina
technologies. Sci Data 6, 285 (2019).

- **CamiSim**: Fritz, A., Lesker, T., Bremges, A. & McHardy, A. Cami 2 - multisample benchmark dataset of human microbiome project,
10.4126/FRL01-006425518 (2019).

- **NIST**: Bioproject *PRJNA970731*. SRA Accession *SUB12091075*.

- **Tourlousse**: Tourlousse, D. M. et al. Characterization and demonstration of mock communities as control reagents for accurate
human microbiome community measurements. Microbiol. Spectr. 10, e01915–21, 10.1128/spectrum.01915-21 (2022).
https://journals.asm.org/doi/pdf/10.1128/spectrum.01915-21.

Within each subdirectory are CSVs of ground truth standardized names and expected abundances. The annotated files have TAXIDs attached in the following format: **Species, RA, TAXID**.

### Pipelines
This folder contains the cleaned outputs from the raw pipeline output, as well as the statistics. The folder layout is identical to the **Expected Pipelines**, but there are subdirectories for each pipeline. Also, there is a [threshold]\_all\_stats\_replicates\_[genus/species].csv file, which summarizes the statistics for the community across all of the pipelines.

### Python_Src
This folder contains much of the project's code to convert raw data into data that can be analyzed. There are several subdirectories here. Omitted subdirectories were not needed for this project. There is also useful information about each pipeline individually in the [Pipelines](docs/pipelines.md) file.

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
    - `databases`: where the NCBI database should go (i.e., from https://ftp.ncbi.nih.gov/pub/taxonomy/new_taxdump/) and uncompress it.
    - `pkls`: initially empty folder -- where the standardized outputs will go from the NCBI parsing routine.
    - `names`: contains the name standardization functions
    - `lineage.py/.ipynb`: determines the correct genus name from TAXID.
    - `jams_convert.py`: annotates non-Excel JAMS output.
    - `species_annotated_to_genus`: converts all of the species-level annotated RA tables to genus-level.

- `paper`: diagrams and figures for the manuscript.
    - `heatmaps.ipynb`: creates the RA table comparison heatmaps.
    - `read_stats.ipynb`: creates and analyzes read stats tables

- `time`: calculates the time performance of each pipeline.

- `data_paths.py`: holds the path to the raw data on the Biowulf computing cluster. 

    - **Note**: for running this analysis, the tarball `mock_communities.tar.gz` holds the raw data locally. If you would like to recreate this analysis, you will need to extract this archive. Extract the archive in the `utils` directory.

            tar -xzf mock_communities.tar.gz 
    
        This will recreate the supercomputer's file structure with the necessary files in a directory named `Volumes`. 

# Data Sources for Figures and Tables
- The main sources of data can be found in the `data_paths.py` explanation. However, if you wish to conduct your own analysis, may be easier to use the data found in `expected_pipelines` and `pipelines`, since these have been transformed into RA values and standardized with TAXIDs. 

## Figures 1 and 7
These flow charts were generated using [diagrams.net](https://diagrams.net).

## Figures 2 and 3
The heatmaps were generated using the [heatmaps.ipynb](/utils/paper/heatmaps.ipynb) notebook with the raw data sourced from the `expected_pipelines` and `pipelines` folders.

## Figures 4 and 5
These figures were generated from the [analyze_stats.ipynb](/utils/analysis/analyze_stats.ipynb) notebook, which also created the [all_stats_species.csv](/utils/analysis/results/all_stats_species.csv) data.

- Additionally, the pairwise Wilcoxon test analysis is conducted in the same file.

## Figure 6
The bivariate plot was generated using the [read_AD.ipynb](/utils/analysis/ad_vs_reads/read_AD.ipynb).

## Table 1
The original read statistics CSV file can be found at [read_stats.csv](/utils/paper/read_stats.csv).

## Tables 2, 3, 4
These metrics were calculated from [figures.ipynb](/figures.ipynb), which generated the `all_stats` files in the `pipelines` folders. Then, the [tables.ipynb](/utils/analysis/summary_tables/tables.ipynb) notebook was used to generate the wanted format. These were then cleaned manually and placed into [ad_table.xlsx](/utils/paper/ad_table_04062023.xlsx) for easy transformation into LaTeX tables.

## Table 5
These tables were generated from the NIST confusion matrix analysis at [nist_sens.ipynb](/python_src/nist_confusion/nist_sens.ipynb) and further cleaning was done with 