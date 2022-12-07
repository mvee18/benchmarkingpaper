# Pipelines
## Biobakery
### Usage
1. Run on Biowulf using the `bake.sh` script in the `scripts/bio` folder. Make sure to change input extension if necessary or pair identifer.
2. Run the `cut.sh` script to grab the species relative abundances.
3. Point the `data_path` variable to the file generated in the previous step. 
4. Run the notebook. This should generate a csv for each column (sample) in the taxonomic profile. It will also attach the tax_id for usage in analysis.

## JAMS
### Usage
#### JAMSalpha
0. Source `~/bash.profile` and then run `getjams`.
1. `JAMSmakeswarm -r [path/to/reads] -d [path/to/db]` This makes the swarm file for submission.
2. You may need to rename the reads to _R1 and _R2 for it to be detected as paired-end. 
3. Submit the swarm files, `swarm -g 246 -t 56 --time=24:00:00 --module R,samtools --gres=lscratch:400 -f JAMS.swarm`.
4. Optional: Use JAMSbankit to move samples to bank. See **JAMSbankit** below.

#### JAMSbankit
1. Make a directory for banking (i.e, BANK).
2. Run `JAMSbankit -d BANK -m -x`. This will move rather than copy and delete the original folders (no longer needed.)

#### JAMSbeta
0. Ensure you have a metadata file in TSV format. See: `https://github.com/johnmcculloch/JAMS_BW/wiki` for more information.
1. Make a new folder for the output, e.g. beta_output.
2. Run `JAMSbeta -p [projectname] -o [output] -t [metadata].tsv -y [path/to/jamsfiles] -e -k -z -n LKT,ECNumber,Product,Pfam,Interpro,GO,resfinder`  
    - The -y flag can be set to `BANK/jamsfiles` if you performed the banking.

#### Analysis
2. Use clean_jams.ipynb to extract RA data and assign taxonomy.

## WGSA
### Usage
1. Run the dataset using Nephele's online platform (`https://nephele.niaid.nih.gov/`).
2. Point `wgsa.ipynb` to the **TEDreadsTAX/reports** folder in the wgsa output.

## Woltka
### Usage
1. Run `wol_decontaminate.py` if the data has host DNA. Submit with `swarm submit_decontaminate.py`. 
2. Run `wol_bowtie.py -i [input/files] -o [output/dir]` If you have different number of CPUS per task, change the optional -t flag.
3. Submit the swarm file: `swarm submit_bowtie.swarm`.
4. Run `wol_classify.py -i [.sam.gz/from/step2] -o [output/dir]`. Submit `sbatch submit_classify.sh`
6. Run `wol_gather_output.ipynb`