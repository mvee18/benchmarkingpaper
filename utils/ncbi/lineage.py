import pandas as pd
import os
from typing import List
import pickle

lineage_pkl_path = os.path.join(
    os.path.dirname(__file__), "pkls", "lineage.pkl")
nodes_pkl_path = os.path.join(os.path.dirname(__file__), "pkls", "nodes.pkl")


def get_lineage_df(path: str, save: bool = False, load_pickle: bool = True) -> pd.DataFrame:
    if load_pickle:
        try:
            return pd.read_pickle(lineage_pkl_path)
        except FileNotFoundError:
            print("Pickle not found. Generating new one.")

    if not os.path.exists(path):
        raise FileNotFoundError("Lineage file does not exist.")

    df = pd.read_csv(path, sep="|", header=None, names=[
                     "tax_id", "parent_tax_id"], dtype=str)

    df.drop("parent_tax_id", axis=1, inplace=True)

    df.reset_index(inplace=True)

    # Remove the \t character from all columns.
    df = df.apply(lambda x: x.str.strip())

    df["tax_id"] = df["tax_id"].str.split(" ")

    rename = {"tax_id": "lineage", "index": "tax_id"}

    df.rename(columns=rename, inplace=True)
    df.set_index("tax_id", inplace=True)

    if save:
        df.to_pickle(lineage_pkl_path)

    return df


def get_parent_ids(tax_id: str, df: pd.DataFrame) -> List[str]:
    """
    Returns a list of tax_ids that are the parents of the given tax_id from the lineage dataframe.
    Parameters:
        tax_id (str): The tax_id to find the parents of.
        df (pd.DataFrame): The lineage dataframe.
    Returns:
        List[str]: A list of tax_ids that are the parents of the given tax_id.
    """
    print(tax_id)
    return df.loc[df.index == tax_id]["lineage"].values[0]

# Now, we need to use the nodes file to determine the rank of each tax_id.


def make_nodes_dict(path: str, save: bool = False, load_pickle: bool = True) -> dict:
    """
    Creates a dictionary of tax_ids and their corresponding rank.
    Parameters:
        path (str): The path to the nodes.dmp file.
    Returns:
        dict: A dictionary of tax_ids and their corresponding rank.
    """
    if load_pickle:
        try:
            return pickle.load(open(nodes_pkl_path, "rb"))
        except FileNotFoundError:
            print("Pickle not found. Generating new one.")

    nodes_dict = {}

    with open(path, "r") as f:
        for line in f:
            line = line.strip().split("|")
            nodes_dict[line[0].strip()] = line[2].strip()

    if save:
        with open(nodes_pkl_path, "wb") as f:
            pickle.dump(nodes_dict, f)

    return nodes_dict


# Now, what we want to do is take the list of tax_ids and find the rank of each one.
def annotate_taxids(taxids: List[str], nodes_dict: dict) -> dict:
    """
    Annotates the tax_ids with their corresponding rank.
    Parameters:
        taxids (List[str]): A list of tax_ids.
        nodes_dict (dict): A dictionary of tax_ids and their corresponding rank.
    Returns:
        dict: A dictionary of tax_ids and their corresponding rank.
    """

    taxids_dict = {}

    for taxid in taxids:
        # print(taxid, nodes_dict[taxid])
        taxids_dict[taxid] = nodes_dict[taxid]

    return taxids_dict


def make_annotation_dataframes():
    lineage_df = get_lineage_df(
        "/Volumes/TBHD_share/DATABASES/NCBI202302/taxidlineage.dmp", save=True, load_pickle=True)
    nodes_dict = make_nodes_dict(
        "/Volumes/TBHD_share/DATABASES/NCBI202302/nodes.dmp", save=True, load_pickle=True)

    return lineage_df, nodes_dict


def make_annotated_lineage(taxid: str, lineage_df: pd.DataFrame, nodes_dict: dict) -> dict:
    return annotate_taxids(get_parent_ids(taxid, lineage_df), nodes_dict)


def cleanup_lineage(lineage: dict, desired_rank: str) -> str:
    """
    Cleans up the lineage dictionary by removing the ranks that are not needed.
    Parameters:
        lineage (dict): A dictionary of tax_ids and their corresponding rank.
    Returns:
        dict: A dictionary of tax_ids and their corresponding rank.
    """
    if desired_rank not in lineage.values():
        print("Desired rank not found in lineage, using last value instead..", lineage)
        # Return the last value in the dictionary.
        result = list(lineage.keys())[-1]
        if result == "2787823":
            # This is the unclassified rank that we are using consistently.
            return "12908"
        else:
            return result

    else:
        for key, value in lineage.items():
            if value == desired_rank:
                return str(key)

# make_annotated_lineage("1415574")
