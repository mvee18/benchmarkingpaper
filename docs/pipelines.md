# Pipelines
## Biobakery
### Usage
1. Run on Biowulf using the `bake.sh` script in the `scripts/bio` folder. Make sure to change input extension if necessary or pair identifer.

2. Run the `cut.sh` script to grab the species relative abundances.

3. Point the `data_path` variable to the file generated in the previous step. 

4. Run the notebook. This should generate a csv for each column (sample) in the taxonomic profile. It will also attach the tax_id for usage in analysis.

## JAMS


## WGSA
### Usage
1. Run the dataset using Nephele's online platform.
2. Point `wgsa.ipynb` to the **TEDreadsTAX/reports** folder in the wgsa output.


## Woltka