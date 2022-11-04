import os
import pandas as pd
from utils.ncbi.names import generate_names_df, find_tax_id, find_names_from_tax_ids, map_and_add_tax_ids, names_db_path
from typing import List, Tuple
import re


# Everything after the second space should be joined together with -.
def fix_name(name: str) -> str:
    splitted = name.split(" ")

    # In indices greater than or equal to 2, replace any special characters with a -.
    for i in range(len(splitted)):
        if i >= 2:
            splitted[i] = re.sub(r"[^a-zA-Z0-9]", "-", splitted[i])

    # Join indices 2 and greater with a -.
    if len(splitted) > 2:
        splitted[2:] = ["-".join(splitted[2:])]

    # Join the list of lists back into a list of strings with "_".
    splitted = "_".join(splitted)

    # Make all the strings uppercase.
    splitted = splitted.upper()

    # Remove any trailing tabs or spaces.
    splitted = splitted.strip()

    return splitted

# The species abundance tables have already been generated. We just need to fix the names and add the tax_ids.


def convert_jams_to_taxid(df: pd.DataFrame, names_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = df.copy()
    # Get index as list.
    index_list = df.index.tolist()
    # Remove all underscores and replace with spaces.
    index_list = [x.replace("_", " ") for x in index_list]

    # Replace "Unclassified" with "sp." if it is not the only name.
    index_list = [x.replace("Unclassified", "sp.") if x !=
                  "Unclassified" else x for x in index_list]

    # Fix names by joning the names after the second space with a -.
    index_list = [fix_name(x) for x in index_list]

    df.index = index_list

    # Now we can add the tax_ids.
    df = map_and_add_tax_ids(df, names_df)

    # Split the dataframe into two dataframes, those with tax_ids and those without.
    df_with_tax_id = df[df["tax_id"].notna()]
    df_without_tax_id = df[df["tax_id"].isna()]

    return df_with_tax_id, df_without_tax_id


if __name__ == "__main__":
    names_df = generate_names_df(names_db_path, load_pickle=True)
    annotated, unknown = convert_jams_to_taxid(
        "../../pipelines/bmock12/jams/s1_species_relabund.csv", names_df)
