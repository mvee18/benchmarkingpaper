from typing import List
import pandas as pd

# Global variables.
names_db_path = "/Volumes/TBHD_share/DATABASES/names.dmp"
example_names = ["Escherichia coli", "E. coli", "Acetivibrio thermocellus"]


def generate_names_df(db_path: str):
    df = pd.read_csv(names_db_path, sep="|", header=None, names=["tax_id", "name_txt", "unique_name", "name_class", "blank"], dtype={
        "tax_id": str, "name_txt": str, "unique_name": str, "name_class": str, "blank": str})
    df.drop("blank", axis=1, inplace=True)
    df.head()

    # Remove the \t character from all columns.
    df = df.apply(lambda x: x.str.strip())

    return df


def find_tax_id(name_list: List[str], names_df: pd.DataFrame) -> List:
    names_dict = {}
    for name in name_list:
        try:
            names_dict[name] = names_df[names_df["name_txt"]
                                        == name]["tax_id"].values[0]
        except IndexError:
            names_dict[name] = None

    return names_dict


def find_names_from_tax_ids(tax_ids: List[str], names_df: pd.DataFrame) -> List:
    tax_id_names_dict = {}

    for tax_id in tax_ids:
        try:
            tax_id_names_dict[tax_id] = list(
                names_df[names_df["tax_id"] == tax_id]["name_txt"].values)
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
    res = find_tax_id(df.index.tolist(), names_df)

    # Add the tax_id to the dataframe.
    df["tax_id"] = df.index.map(res)

    return df


if __name__ == "__main__":
    # Using the bmock12 data for conversion to TaxIDs.
    # Note that the names were changed from the original to be searchable in the names.dmp file.
    # i.e, DSM was removed, HL lowercased.
    species_df_path = "bmock12_names.csv"

    b12 = pd.read_csv(species_df_path, sep=",", dtype={
        "species": str, "tax_id": str}, index_col=0)

    names_df = generate_names_df(names_db_path)
    b12_named = map_and_add_tax_ids(b12, names_df)

    print(b12_named)

    # Save the dataframe to a csv file.
    b12.to_csv("bmock12_tax_ids.csv")
