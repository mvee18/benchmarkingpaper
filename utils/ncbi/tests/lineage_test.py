import sys  # noqa
sys.path.append("../")  # noqa

from lineage import make_annotation_dataframes, make_annotated_lineage


def test_make_annotated_lineage():
    lin_df, nodes_dict = make_annotation_dataframes()
    test_tax = "1415574"

    result = make_annotated_lineage(test_tax, lin_df, nodes_dict)

    want = {
        '131567': 'no rank',
        '2': 'superkingdom',
        '1224': 'phylum',
        '1236': 'class',
        '2887326': 'order',
        '468': 'family',
        '497': 'genus',
        '196806': 'no rank'
    }

    assert result == want
