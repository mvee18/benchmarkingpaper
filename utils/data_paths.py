# This is a collection of all the paths to each data set for easier access.
from dataclasses import dataclass
import os
from os.path import abspath
from os.path import join as pjoin
from typing import List

# Change this path if you are not using the same mounting point.
root = "/Volumes/"


@dataclass
class MockCommData:
    """ 
    Class that holds the path to each pipeline for each mock community tested. 

    Attributes
        biobakery4: str
            Path to the biobakery4 pipeline species_relab.txt file.
        biobakery3: str 
            Path to the biobakery3 pipeline species_relab.txt file.
        jams: str 
            Path to the jams pipeline JAMSbeta output LKT excel file.
        woltka: str 
            Path to the woltka pipeline classify output directory.
        wgsa: str 
            Path to the wgsa pipeline TAXprofiles/TEDreadsTAX output directory.
        path: str
            Path to the directory where the outputs should go.
    """
    biobakery4: str
    jams: str
    woltka: str
    wgsa: str
    biobakery3: str = ""
    jams202212: str = ""
    sunbeam: str = ""
    path: str = ""

    def __post_init__(self):
        # Make sure that each path exists.
        for name, path in self.__dict__.items():
            if self.__dict__[name] == "":
                continue

            # Append the root to the path. This allows for multiple mounting points.
            self.__dict__[name] = os.path.join(root, path)

            if not os.path.exists(self.__dict__[name]):
                raise FileNotFoundError(
                    f"Path {self.__dict__[name]} does not exist.")


def make_path(path):
    return abspath(pjoin(os.path.dirname(__file__), path))


bmock12 = MockCommData(
    biobakery4="TBHD_share/valencia/pipelines/bmock12/biobakery4/metaphlan/merged/species_relab.txt",
    jams="TBHD_share/valencia/pipelines/bmock12/jams/sub_SRR8073716_JAMS/featuretable.csv",
    woltka="TBHD_share/valencia/pipelines/bmock12/woltka/classify/results",
    wgsa="TBHD_share/valencia/pipelines/bmock12/NEPHELE/wgsa2/subset_bmock12/outputs/TAXprofiles/TEDreadsTAX/reports",
    biobakery3="TBHD_share/valencia/pipelines/bmock12/biobakery3/metaphlan/main/species_relab.txt",
    path=make_path("../pipelines/bmock12/"),
)

# TODO: Rerun the biobakery4 pipeline in the NOADAPTERS folder.
camisim = MockCommData(
    biobakery4="TBHD_share/cami_data/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="TBHD_share/cami_data/NOADAPTERS/pipelines/bio3/metaphlan/merged/species_relab.txt",
    # You have to use the two samples in here manually (s1, s2).
    jams="TBHD_share/cami_data/NOADAPTERS/pipelines/jams/beta_output/cami_Relabund_PPM.xlsx",
    woltka="TBHD_share/cami_data/NOADAPTERS/pipelines/woltka/classify",
    wgsa="TBHD_share/cami_data/NOADAPTERS/pipelines/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/camisimGI/"),
)

tourlousse = MockCommData(
    biobakery4="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/bio3/metaphlan/merged/species_relab.txt",
    jams="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/jams/beta_output/tourlousse_Relabund_PPM.xlsx",
    jams202212="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/jams2022/beta_output/filtered_PPM.xlsx",
    woltka="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/woltka/classify",
    wgsa="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    sunbeam="TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/sunbeam4/sunbeam_output/classify/kraken/",
    path=make_path("../pipelines/tourlousse/"),
)

amos_mixed = MockCommData(
    biobakery4="TBHD_share/valencia/pipelines/amos/nibsc/mixed/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="TBHD_share/valencia/pipelines/amos/nibsc/mixed/bio3/metaphlan/merged/species_relab.txt",
    jams="TBHD_share/valencia/pipelines/amos/nibsc/mixed/jams/beta_output/amos_mixed_Relabund_PPM.xlsx",
    jams202212="TBHD_share/valencia/pipelines/amos/nibsc/mixed/jams2022/beta_output/filtered_PPM.xlsx",
    woltka="TBHD_share/valencia/pipelines/amos/nibsc/mixed/wol/classify",
    wgsa="TBHD_share/valencia/pipelines/amos/nibsc/mixed/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/amos/mixed/"),
)

amos_hilo = MockCommData(
    biobakery4="TBHD_share/valencia/pipelines/amos/nibsc/hilo/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="TBHD_share/valencia/pipelines/amos/nibsc/hilo/bio3/metaphlan/merged/species_relab.txt",
    jams="TBHD_share/valencia/pipelines/amos/nibsc/hilo/jams/beta_output/hilo_Relabund_PPM.xlsx",
    jams202212="TBHD_share/valencia/pipelines/amos/nibsc/hilo/jams2022/beta_output/filtered_PPM.xlsx",
    woltka="TBHD_share/valencia/pipelines/amos/nibsc/hilo/woltka/classify",
    wgsa="TBHD_share/valencia/pipelines/amos/nibsc/hilo/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/amos/hilo/"),
)

hmpGut = MockCommData(
    biobakery4="",
    biobakery3="TBHD_share/valencia/pipelines/HMP/gut/bio3/metaphlan/merged/species_relab.txt",
    jams="TBHD_share/valencia/pipelines/HMP/gut/jams/beta_output/guthmp_Relabund_PPM.xlsx",
    woltka="TBHD_share/valencia/pipelines/HMP/gut/wol/classify",
    wgsa="TBHD_share/valencia/pipelines/HMP/gut/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/hmp/gut/"),
)

# hmpTongue = MockCommData(
#     biobakery4="TBHD_share/valencia/pipelines/HMP/tongue/bio4/metaphlan/merged/species_relab.txt",
#     jams="TBHD_share/valencia/pipelines/HMP/tongue/jams/beta/hmp_tongue_Relabund_PPM.xlsx",
#     woltka="",
#     wgsa="TBHD_share/valencia/pipelines/HMP/tongue/wgsa2/outputs/TAXprofiles/TEDreadsTAX/reports",
#     path=make_path("../pipelines/hmp/tongue/"),
# )

nist = MockCommData(
    biobakery4="TBHD_share/valencia/pipelines/NIST/pipelines/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="TBHD_share/valencia/pipelines/NIST/pipelines/bio3/metaphlan/merged/species_relab.txt",
    jams="TBHD_share/valencia/pipelines/NIST/pipelines/jams/beta_output/NIST_Relabund_PPM.xlsx",
    woltka="TBHD_share/valencia/pipelines/NIST/pipelines/woltka/classify",
    wgsa="TBHD_share/valencia/pipelines/NIST/pipelines/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/nist/"),
)


def make_data_list() -> List[MockCommData]:
    """Return a list of all the mock community data objects."""
    return [
        bmock12, camisim, tourlousse,
        amos_mixed, amos_hilo, hmpGut, nist]


if __name__ == "__main__":
    for data in make_data_list():
        print(data, "\n")
