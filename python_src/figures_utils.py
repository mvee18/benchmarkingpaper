import pandas as pd
import os


def get_all_expected(root_dir: str, rank="Genus") -> pd.DataFrame:
    combined_expected = pd.DataFrame()
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            # print("files: ", files)
            if f"expected_{rank.lower()}_annotated" in f and f.endswith(".csv"):
                # print(f)
                df = pd.read_csv(os.path.join(root, f), index_col=0, names=[
                                 rank, 'RA', "TAX_ID"], header=0)
                # df["Source"] = root.split("/")[-1]
                df["Source"] = "Expected"

                # Files are of s#_expected.csv, so we can split on the underscore and take the first part.
                df["SampleID"] = f.split("_")[0]
                combined_expected = pd.concat([combined_expected, df], axis=0)

    return combined_expected


def generate_experimental_df(input_path: str, index_name: str) -> pd.DataFrame:
    """
    Parameters:
        input_path: str
            Path to the experimental abundance file.
        index_name: str
            The name of the index column.
    Returns:
        experimental: pd.DataFrame
            The experimental abundances in a dataframe. The format is | rank | abundance | TAX_ID |.

    Reads the csv and generates a dataframe from the experimental results.
    """
    # Now, load in the experimental values.
    r_genus = pd.read_csv(input_path, index_col=0, names=[
                          index_name, "RA", "TAX_ID"], header=0)
    # display(r_genus.head(12))
    r_genus = r_genus.astype({'RA': 'float64', 'TAX_ID': 'int64'})

    return r_genus


def get_relabund_files(root_dir: str, rank="genus") -> pd.DataFrame:
    """
    Parameters:
        root_dir: str 
            The root directory to search for relabund files.
        rank: str
            The taxonomic rank to search for. Default is "genus".
    Returns:
        relabund_files: pd.DataFrame

    Traverses the root directory and searches for {rank}_relabund_annotated files. These are concatenated. \\
    Then, it then returns a dataframe with the sample ID and the path to the relabund file.
    """
    combined_df = pd.DataFrame()
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f"{rank.lower()}_relabund_annotated" in f and f.endswith(".csv"):
                # print(root, f)
                p = os.path.join(root, f)
                exp = generate_experimental_df(p, rank)

                # Add a column to the experimental dataframe with the pipeline name.
                exp['Source'] = os.path.dirname(p).split('/')[-1]

                # Add sampleID to the experimental dataframe.
                exp['SampleID'] = os.path.basename(p).split('_')[0]
                # display(exp.head(10))

                # Add the experimental dataframe to the combined dataframe.
                combined_df = pd.concat([combined_df, exp], axis=0)

    # Ensure that the RA column is a float.
    combined_df['RA'] = combined_df['RA'].astype(float)

    return combined_df


def fully_combined(root_dir: str, rank: str, get_rel_func: callable = get_relabund_files, get_all_exp_func: callable = get_all_expected) -> pd.DataFrame:
    """
    Parameters:
        root_dir: str
            The root directory to search for relabund files.
        rank: str
            The taxonomic rank to search for. Default is "genus".
        get_rel_func: callable
            The function to use to get the relative abundance files. Default is get_relabund_files.
        get_all_exp_func: callable
            The function to use to get the expected abundance files. Default is get_all_expected.
    Returns:
        combined_df: pd.DataFrame

    Gathers all expected and experimental dataframes and combines them into a single dataframe.
    """
    if rank is None:
        raise Exception("Rank is not defined.")

    combined_df = get_rel_func(root_dir, rank=rank)

    combined_expected = get_all_exp_func(root_dir, rank=rank)

    # Merge the expected and experimental dataframes.
    merged = pd.concat([combined_expected, combined_df], axis=0)
    merged = merged.reset_index()
    merged = merged.rename(columns={'index': rank})

    # merged = merged.astype({'TAX_ID': 'int64'})
    merged = merged.set_index("TAX_ID")

    # display(merged.head())
    # merged.to_csv("combined.csv", index=True, index_label="TAX_ID")

    return merged
