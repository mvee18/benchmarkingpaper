import os
import argparse

"""
This program will take a directory of user-specified files and create a swarm file to run fastp on them.
This is for use with paired-end reads.
The fastp parameters (different from the default) are:
    -cut_front
    -cut_tail

"""

parser = argparse.ArgumentParser(
    description='Gather WOL data from Woltka classify.')
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Input dir.')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Output directory.')
parser.add_argument('-e', '--extension', type=str,
                    required=False, default="fastq", help='File extension.')
parser.add_argument('-q', '--quality', type=int, required=False,
                    default=15, help='Quality score to trim to.')
args = parser.parse_args()

data_dir = args.input


def find_files(data_dir, extension):
    """Find files in directory.

    Parameters
    ----------
    data_dir : str
        Path to directory containing output files.
    extension : str
        File extension.

    Returns
    -------
    list
        List of paths to output files.
    """
    output_files = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(extension):
                output_files.append(os.path.join(root, file))
    return output_files


if __name__ == "__main__":
    files = find_files(data_dir, args.extension)
    files.sort()

    output_file = os.path.join(args.output, "fastp.swarm")

    # Group every two files together for a list of tuples.
    files_tuples = [files[i:i + 2] for i in range(0, len(files), 2)]
    # print(files_tuples)

    with open(output_file, "w") as f:
        for i in files_tuples:
            out1 = os.path.abspath(os.path.join(
                args.output, os.path.basename(i[0]).split(".")[0]))
            out2 = os.path.abspath(os.path.join(
                args.output, os.path.basename(i[1]).split(".")[0]))
            f.write(
                f"fastp -i {os.path.abspath(i[0])} -I {os.path.abspath(i[1])} -o {out1}.fastp.fastq -O {out2}.fastp.fastq -q {args.quality} --cut_front --cut_tail -l 100\n")
