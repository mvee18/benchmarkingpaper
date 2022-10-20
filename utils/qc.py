import os
import argparse

parser = argparse.ArgumentParser(
    description='Gather WOL data from Woltka classify.')
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Input dir.')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Output directory.')
parser.add_argument('-e', '--extension', type=str,
                    required=True, default="fastq", help='File extension.')
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

    swarm_file = os.path.join(os.path.abspath(args.output), "qc.swarm")

    with open(swarm_file, "w") as f:
        for i in files:
            f.write(
                f"fastqc {os.path.abspath(i)} -o {os.path.abspath(args.output)}\n")
