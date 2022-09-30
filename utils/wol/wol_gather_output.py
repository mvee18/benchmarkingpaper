import os
import pandas as pd
import argparse

# Add arguments for input and output.
parser = argparse.ArgumentParser(description='Gather WOL data from Woltka classify.')
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Input dir.')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Output directory.')
args = parser.parse_args() 

data_dir = args.input

def find_output_files(rank, data_dir):
    """Find output files from Woltka classify.
    
    Parameters
    ----------
    rank : str
        Taxonomic rank.
    data_dir : str
        Path to directory containing output files.
    
    Returns
    -------
    list
        List of paths to output files.
    """
    output_files = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if f"{rank}.tsv" == file:
                output_files.append(os.path.join(root, file))
    return output_files

def rel_abundance(df, output, rank, plot=False):
    df.drop("FeatureID", axis=1, inplace=True)
    # pct = df[["Count"]].apply(lambda x: x / x.sum(), axis=0)
    df["RA"] = df["Count"] / df["Count"].sum()
    df.drop("Count", axis=1, inplace=True)
    df = df.sort_values(by="RA", ascending=False)

    # Remove any [ and ] from the index.
    df.index = df.index.str.replace("[", "", regex=False)
    df.index = df.index.str.replace("]", "", regex=False)
    # display(df.head())

    df.to_csv(output, sep=",")
    df = df.where(df > 0.001).dropna()

    if plot:
        df.T.plot.bar(figsize=(10,10), xlabel="{rank} Name", ylabel="Fraction", title=f"{rank} Relative Abundance above 0.1%").legend(loc='center left', bbox_to_anchor=(1.0, 0.5), title=f"{rank}")
        plt.savefig(output + ".png", bbox_inches='tight')

# Find output files.
def find_and_save(input_data: str, rank: str, output_dir: str):
    """Find and save output files from Woltka classify.
    
    Parameters
    ----------
    input_data : str
        Path to directory containing output files.
    rank : str
        Taxonomic rank.
    output_dir : str
        Path to directory to save output files.
    """
    output_files = find_output_files(rank, input_data)
    for file in output_files:
        print(file)
        df = pd.read_csv(file, sep="\t", names=["FeatureID", "Count", "Species"], header=0, index_col=2)

        sampleID = (os.path.dirname(file).split("/")[-1]).split("_")[0]
        output_path = os.path.join(output_dir, f"{sampleID}_{rank}_relabund.csv")
        rel_abundance(df, output_path, rank)
    
find_and_save(data_dir, "genus", args.output)
