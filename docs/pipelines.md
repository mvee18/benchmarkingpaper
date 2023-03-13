# Running QC & Pipelines
## Requirements
- These scripts were developed for the NIH supercomputer, Biowulf, which uses the SLURM queuing system. Any HPC using SLURM should be able to run these input files. 
- A working JAMS installation, which currently only supports Biowulf installations (see https://github.com/johnmcculloch/JAMS_BW).
- A Nephele account (https://nephele.niaid.nih.gov/). A Globus account linked to the storage location of the samples is also highly beneficial (https://www.globus.org/).

## Quality Control 
---


## Preferred Method for Pipelines
---
The best way of running this pipeline is to first use the automated script, located at `scripts/do_pipeline/main.py`. This is a separate git repo, located at https://github.com/mvee18/BiowulfUtils.

This will generate the input files for Biobakery4, JAMS, and Woltka. Then, you will need to follow the steps below for each pipeline.

## Biobakery
### Usage
1.  Submit the generated `bio4.sh` file, typically using:

        sbatch bio4.sh

    Make sure to change input extension or pair identifer if necessary.
2. Run the `cut.sh` script to grab the species relative abundances (`scripts/bio/cut.sh`). Use `cut_bio4.sh` for MetaPhlAn4 outputs.

3. Point the MockCommData object in `utils/data_path.py` to the file generated in the previous step. 

4. Run the notebook (`python_src/pipeline_clean/biobakery.ipynb`). This should generate a csv for each column (sample) in the taxonomic profile. It will also attach the tax_id for usage in analysis.

## JAMS
### Usage
#### JAMSalpha
0. Source `~/bash.profile` and then run `getjams`.
1. `JAMSmakeswarm -r [path/to/reads] -d [path/to/db]` This makes the swarm file for submission.
2. You may need to rename the reads to _R1 and _R2 for it to be detected as paired-end. 
3. Submit the swarm files:

        swarm -g 246 -t 56 --time=24:00:00 --module R,samtools --gres=lscratch:400 -f JAMS.swarm.

4. Optional: Use JAMSbankit to move samples to bank. See **JAMSbankit** below.

#### JAMSbankit
1. Make a directory for banking (i.e, BANK).
2. Run `JAMSbankit -d BANK -m -x`. This will move rather than copy and delete the original folders (no longer needed.)

#### JAMSbeta
0. Ensure you have a metadata file in TSV format. See: `https://github.com/johnmcculloch/JAMS_BW/wiki` for more information.
1. Make a new folder for the output, e.g. beta_output.
2. Run 

        JAMSbeta -p [projectname] -o [output] -t [metadata].tsv -y [path/to/jamsfiles] -e -k -z -n LKT,ECNumber,Product,Pfam,Interpro,GO,resfinder
    
    - The -y flag can be set to `BANK/jamsfiles` if you performed the banking.

#### Analysis
1. Point the `utils/data_paths.py` file to the output Excel file with "LKT_relabund" in the name.
2. Run the `python_src/clean_pipelines/clean_jams.ipynb` file.

## WGSA
### Usage
1. Run the dataset using Nephele's online platform (`https://nephele.niaid.nih.gov/`).
2. Point the MockCommData object in `utils/data_path.py` to the TAXprofiles/TEDreadsTAX directory generated in the previous step. 
3. Run `python_src/clean_pipelines/clean_wgsa.ipynb`.

## Woltka
### Usage
1. Run `wol_decontaminate.py` if the data has host DNA. Submit with `swarm submit_decontaminate.py`. 
2. Submit the swarm file: `swarm submit_bowtie.swarm`.
3. Wait for the jobs from step 2 to complete.
4. Submit `sbatch submit_classify.swarm` (located in the classify directory).
5. Point the MockCommData object in `utils/data_path.py` to the "classify" directory generated in the previous step. 
6. Run `wol_gather_output.ipynb`