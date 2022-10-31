from names import generate_names_df, find_tax_id, names_db_path, standardize
import pandas as pd


def test_find_tax_id():
    example_names = {"AEROMONAS_SP._Y301-2": 2990505,
                     "ESCHERICHIA_COLI": 562}

    names_df = generate_names_df(names_db_path, pickle=False, load_pickle=True)

    res = find_tax_id(list(example_names.keys()), names_df)

    assert res == example_names


def test_standardized():
    example_ncbi = pd.DataFrame(
        {'tax_id': [1], 'name_txt': ["Psychrobacter sp. CCUG 69069"]})

    example_ncbi = standardize(example_ncbi)

    assert example_ncbi["split_name"].values[0] == "PSYCHROBACTER_SP._CCUG-69069"
