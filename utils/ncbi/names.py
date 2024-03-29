from typing import List, Callable
import pandas as pd
import re
import os
from datetime import datetime, timezone

# Global variables.
# Expect the names.dmp file to be in the same directory as this file.
names_db_path = os.path.abspath(os.path.join("utils", "ncbi", "databases", "names.dmp"))
# print(names_db_path)
example_names = ["Escherichia coli", "E. coli", "Acetivibrio thermocellus"]


def standardize_core(
    input_df: pd.DataFrame, split_names: List[List[str]]
) -> pd.DataFrame:
    """
    Standardizes the names in the dataframe from the provided split names.
    This will replace all non-alphanumeric characters with a -. Any strain data will be joined with a -.
    Also, all names will be converted to uppercase and joined with a _.
    """
    # In indices greater than or equal to 2, replace any special characters or spaces with a -.
    for i in range(len(split_names)):
        for j in range(len(split_names[i])):
            if j >= 2:
                split_names[i][j] = re.sub(r"[^a-zA-Z0-9]", "-", split_names[i][j])

    for i in range(len(split_names)):
        if len(split_names[i]) > 2:
            split_names[i] = split_names[i][:2] + ["-".join(split_names[i][2:])]

    # Remove any [ or ] characters.
    for i in range(len(split_names)):
        for j in range(len(split_names[i])):
            split_names[i][j] = re.sub(r"[\[\]]", "", split_names[i][j])

    # Join the list of lists back into a list of strings with "_".
    split_names = ["_".join(x) for x in split_names]

    # Make all the strings uppercase.
    split_names = [x.upper() for x in split_names]

    # Add the split names to the dataframe.
    input_df["split_name"] = split_names

    return input_df


def standardize_ncbi(ncbi_df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes the NCBI data using the standardize_core function.
    """
    df = ncbi_df.copy()
    names = df["name_txt"].tolist()
    split_names = [x.split() for x in names]

    df = standardize_core(df, split_names)

    final_result = df[["tax_id", "name_txt", "split_name"]]

    # All of the tax_id should be integers.
    casted = final_result.astype({"tax_id": int})

    return casted


def generate_names_df(db_path: str, pickle=False, load_pickle=False) -> pd.DataFrame:
    """
    Generates a dataframe from the names.dmp file from NCBI.
    Parameters
    ----------
    db_path : str
        The path to the names.dmp file.
    pickle : bool, optional
        Whether to pickle the dataframe, by default False.
    load_pickle : bool, optional
        Whether to load the pickle, by default False
    """
    # Let's print the time the pkl file was last modified in case the database is old.
    pkl_path = os.path.join(os.path.dirname(__file__), "pkls", "names_df.pkl")

    if load_pickle:
        if os.path.exists(pkl_path):
            stat = os.stat(pkl_path)
            modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            print(
                "The pkl file was last modified (and hopefully generated) on {}".format(
                    modified
                )
            )

            names_df = pd.read_pickle(pkl_path)
            return names_df
        else:
            print("Pickle does not exist. Generating dataframe from names.dmp.")

    df = pd.read_csv(
        db_path,
        sep="|",
        header=None,
        names=["tax_id", "name_txt", "unique_name", "name_class", "blank"],
        dtype={
            "tax_id": str,
            "name_txt": str,
            "unique_name": str,
            "name_class": str,
            "blank": str,
        },
    )
    df.drop("blank", axis=1, inplace=True)
    df.head()

    # Remove the \t character from all columns.
    df = df.apply(lambda x: x.str.strip())

    df = standardize_ncbi(df)

    if pickle:
        df.to_csv("pkls/names_df.csv", index=False)
        df.to_pickle(pkl_path)

    return df


def find_tax_id(name_list: List[str], names_df: pd.DataFrame) -> List:
    names_dict = {}
    for name in name_list:
        try:
            names_dict[name] = names_df[names_df["split_name"] == name][
                "tax_id"
            ].values[0]
        except IndexError:
            names_dict[name] = None

    return names_dict


def find_names_from_tax_ids(tax_ids: List[str], names_df: pd.DataFrame) -> List:
    tax_id_names_dict = {}

    for tax_id in tax_ids:
        try:
            tax_id_names_dict[tax_id] = list(
                names_df[names_df["tax_id"] == tax_id]["split_name"].values
            )
        except IndexError:
            tax_id_names_dict[tax_id] = None

    return tax_id_names_dict


def map_and_add_tax_ids(df: pd.DataFrame, names_df: pd.DataFrame) -> pd.DataFrame:
    """Maps the names in the index of the dataframe to tax_ids and adds them to the dataframe.

    Args:
        df (pd.DataFrame): The dataframe to map the names to tax_ids.
        names_df (pd.DataFrame): The dataframe containing the names and tax_ids.

    Returns:
        pd.DataFrame: The dataframe with the tax_ids added.
    """
    res = find_tax_id(df.index.to_list(), names_df)

    # Add the tax_id to the dataframe.
    df["tax_id"] = df.index.map(res)

    return df


# Conversion functions for the convert_expected function by pipeline.
def split_jams(exp_df: pd.DataFrame) -> List[List[str]]:
    exp_names = exp_df.index.tolist()
    exp_split_names = [x.split() for x in exp_names]

    return exp_split_names


def split_bio(exp_df: pd.DataFrame) -> List[List[str]]:
    exp_names = exp_df.index.tolist()

    # print(exp_names)
    # Replace any instance of sp with sp.
    exp_names = [re.sub("_sp_", "_sp._", x) for x in exp_names]

    # There is also a case where sp is at the end, so replace that too.
    exp_names = [re.sub("_sp$", "_sp.", x) for x in exp_names]

    # print(exp_names)

    exp_split_names = [x.split("_") for x in exp_names]

    return exp_split_names


def convert_expected(data_path: str, split_func: Callable) -> pd.DataFrame:
    """
    Takes a dataframe, loads the NCBI names, splits the dataframe names according to the parameters function
        then, standardizes the list of names and adds the tax ids.

    ## Parameters
        data_path : str
            The path to the expected data.
        split_func : Callable
            The function to split the names. Should take in a dataframe and return a list of lists.

    ## Returns:
        pd.DataFrame
            The dataframe with the tax_ids added.
    """
    # Experimental dataframe.
    exp_df = pd.read_csv(
        data_path, sep=",", dtype={"species": str, "tax_id": str}, index_col=0
    )

    # Generate the names dataframe.
    ncbi_df = generate_names_df(names_db_path, load_pickle=True)

    # Names from the experimental dataframe that need to be standardized.
    exp_split_names = split_func(exp_df)

    # Standardize the names. Set the index to the standardized names.
    standardized_exp = standardize_core(exp_df, exp_split_names)
    print(standardized_exp)
    standardized_exp.set_index("split_name", inplace=True)

    # Map the standardized names to tax_ids.
    exp_with_taxid = map_and_add_tax_ids(standardized_exp, ncbi_df)

    # Check if any tax_ids are missing. If so, raise an exception.
    if exp_with_taxid["tax_id"].isnull().values.any():
        # Print the names that are missing tax_ids.
        print(exp_with_taxid[exp_with_taxid["tax_id"].isnull()])
        raise Exception("Missing tax_ids. Check the names.")

    exp_with_taxid = exp_with_taxid.astype({"tax_id": int})

    # Save the dataframe to a csv file.
    file_name = os.path.basename(data_path).split(".")[0]

    if "genus" in file_name:
        output_path = os.path.join(
            os.path.dirname(data_path), f"{file_name}_annotated.csv"
        )
        exp_with_taxid.to_csv(output_path, index_label="Genus")

    elif "species" in file_name:
        # print(exp_with_taxid)
        output_path = os.path.join(
            os.path.dirname(data_path), f"{file_name}_annotated.csv"
        )
        exp_with_taxid.to_csv(output_path, index_label="Species")

    else:
        raise Exception("File name must contain genus or species.")

    return exp_with_taxid


if __name__ == "__main__":
    pass
    # Using the bmock12 data for conversion to TaxIDs.
    # Note that the names were changed from the original to be searchable in the names.dmp file.
    # i.e, DSM was removed.
    if not os.path.exists(names_db_path):
        raise Exception(
            "names.dmp file does not exist. Expected at {}".format(names_db_path)
        )

    generate_names_df(names_db_path, pickle=True)

    # species_df_path = "../../pipelines/amos/mixed/expected_species.csv"
    # convert_expected(species_df_path, split_jams)
