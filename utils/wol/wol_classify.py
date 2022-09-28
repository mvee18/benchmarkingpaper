import os
import argparse

# Parse arguments for input and output.
parser = argparse.ArgumentParser(description='Classify WOL data.')
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Input file.')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Output dir.')
args = parser.parse_args()

sam_files = []
for file in os.listdir(args.input):
    if file.endswith(".sam.gz"):
        sam_files.append(os.path.join(args.input, file))

line = """woltka classify -i {} --to-tsv -o {}_classify -r genus,species --map /gpfs/gsfs12/users/TBHD_share/valencia/pipelines/woltka/db/taxonomy/taxid.map --nodes /gpfs/gsfs12/users/TBHD_share/valencia/pipelines/woltka/db/taxonomy/nodes.dmp --names /gpfs/gsfs12/users/TBHD_share/valencia/pipelines/woltka/db/taxonomy/names.dmp"""

with open("submit_classify.sh", "w") as f:
    f.write("#!/bin/bash\n\n")
    f.write("# SBATCH --mem=64gb\n")
    f.write("# SBATCH --cpus-per-task=16\n\n")

    for file in sam_files:
        print(file)
        id = file.split("/")[-1].split(".")[0]
        output = os.path.join(args.output, id)
        line = line.format(file, output)
        f.write(line + "\n")
