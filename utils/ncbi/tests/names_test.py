from names import generate_names_df, find_tax_id, names_db_path, standardize_ncbi, convert_expected, split_jams
import pandas as pd


def test_standardized():
    example_ncbi = pd.DataFrame(
        {'tax_id': [1, 2], 'name_txt': ["Psychrobacter sp. CCUG 69069", "Escherichia coli"]})

    example_ncbi = standardize_ncbi(example_ncbi)

    assert example_ncbi["split_name"].values[0] == "PSYCHROBACTER_SP._CCUG-69069"
    assert example_ncbi["split_name"].values[1] == "ESCHERICHIA_COLI"


def test_bmock12_expected():
    species_df_path = "test_data/bmock12/S1_expected_species.csv"
    got_df = convert_expected(species_df_path, split_jams)
    got_df = got_df[["tax_id"]]

    want_df = pd.read_csv(
        "test_data/bmock12/S1_expected_species_annotated.csv", index_col=0)
    want_df = want_df[["tax_id"]]

    assert got_df.equals(want_df)


def test_find_tax_id():
    example_names = {"AEROMONAS_SP._Y301-2": 2990505,
                     "ESCHERICHIA_COLI": 562}

    names_df = generate_names_df(
        names_db_path, pickle=False, load_pickle=True)

    res = find_tax_id(list(example_names.keys()), names_df)

    assert res == example_names
