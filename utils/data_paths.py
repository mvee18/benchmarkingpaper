# This is a collection of all the paths to each data set for easier access.
from dataclasses import dataclass
import os
from os.path import abspath
from os.path import join as pjoin
from typing import List


@dataclass
class MockCommData:
    """ Class that holds the path to each pipeline for each mock community tested. """
    biobakery4: str
    jams: str
    woltka: str
    wgsa: str
    biobakery3: str = ""
    jams202212: str = ""
    path: str = ""

    def __post_init__(self):
        # Make sure that each path exists.
        for path in self.__dict__.values():
            if path == "":
                continue
            if not os.path.exists(path):
                raise FileNotFoundError(f"Path {path} does not exist.")


def make_path(path):
    return abspath(pjoin(os.path.dirname(__file__), path))


bmock12 = MockCommData(
    biobakery4="/Volumes/TBHD_share/valencia/pipelines/bmock12/biobakery4/metaphlan/merged/species_relab.txt",
    jams="/Volumes/TBHD_share/valencia/pipelines/bmock12/jams/sub_SRR8073716_JAMS/featuretable.csv",
    woltka="/Volumes/TBHD_share/valencia/pipelines/bmock12/woltka/classify/results",
    wgsa="/Volumes/TBHD_share/valencia/pipelines/bmock12/NEPHELE/wgsa2/subset_bmock12/outputs/TAXprofiles/TEDreadsTAX/reports",
    biobakery3="/Volumes/TBHD_share/valencia/pipelines/bmock12/biobakery3/metaphlan/main/species_relab.txt",
    path=make_path("../pipelines/bmock12/"),
)

# TODO: Rerun the biobakery4 pipeline in the NOADAPTERS folder.
camisim = MockCommData(
    biobakery4="/Volumes/TBHD_share/cami_data/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="/Volumes/TBHD_share/cami_data/NOADAPTERS/pipelines/bio3/metaphlan/merged/species_relab.txt",
    # You have to use the two samples in here manually (s1, s2).
    jams="/Volumes/TBHD_share/cami_data/NOADAPTERS/pipelines/jams/beta_output/cami_Relabund_PPM.xlsx",
    woltka="/Volumes/TBHD_share/cami_data/NOADAPTERS/pipelines/woltka/classify",
    wgsa="/Volumes/TBHD_share/cami_data/NOADAPTERS/pipelines/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/camisimGI/"),
)

tourlousse = MockCommData(
    biobakery4="/Volumes/TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="/Volumes/TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/bio3/metaphlan/merged/species_relab.txt",
    jams="/Volumes/TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/jams/beta_output/tourlousse_Relabund_PPM.xlsx",
    jams202212="/Volumes/TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/jams2022/beta_output/tourlousse_Relabund_PPM.xlsx",
    woltka="/Volumes/TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/woltka/classify",
    wgsa="/Volumes/TBHD_share/valencia/pipelines/microbio_spectrum/CLEANED/pipelines/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/tourlousse/"),
)

amos_mixed = MockCommData(
    biobakery4="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/mixed/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/mixed/bio3/metaphlan/merged/species_relab.txt",
    jams="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/mixed/jams/beta_output/amos_mixed_Relabund_PPM.xlsx",
    jams202212="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/mixed/jams2022/beta_output/mixed_Relabund_PPM.xlsx",
    woltka="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/mixed/wol/classify",
    wgsa="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/mixed/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/amos/mixed/"),
)

amos_hilo = MockCommData(
    biobakery4="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/hilo/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/hilo/bio3/metaphlan/merged/species_relab.txt",
    jams="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/hilo/jams/beta_output/hilo_Relabund_PPM.xlsx",
    jams202212="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/hilo/jams2022/beta_output/hilo_Relabund_PPM.xlsx",
    woltka="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/hilo/woltka/classify",
    wgsa="/Volumes/TBHD_share/valencia/pipelines/amos/nibsc/hilo/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/amos/hilo/"),
)

hmpGut = MockCommData(
    biobakery4="",
    biobakery3="/Volumes/TBHD_share/valencia/pipelines/HMP/gut/bio3/metaphlan/merged/species_relab.txt",
    jams="/Volumes/TBHD_share/valencia/pipelines/HMP/gut/jams/beta_output/guthmp_Relabund_PPM.xlsx",
    woltka="/Volumes/TBHD_share/valencia/pipelines/HMP/gut/wol/classify",
    wgsa="/Volumes/TBHD_share/valencia/pipelines/HMP/gut/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/hmp/gut/"),
)

# hmpTongue = MockCommData(
#     biobakery4="/Volumes/TBHD_share/valencia/pipelines/HMP/tongue/bio4/metaphlan/merged/species_relab.txt",
#     jams="/Volumes/TBHD_share/valencia/pipelines/HMP/tongue/jams/beta/hmp_tongue_Relabund_PPM.xlsx",
#     woltka="",
#     wgsa="/Volumes/TBHD_share/valencia/pipelines/HMP/tongue/wgsa2/outputs/TAXprofiles/TEDreadsTAX/reports",
#     path=make_path("../pipelines/hmp/tongue/"),
# )

nist = MockCommData(
    biobakery4="/Volumes/TBHD_share/valencia/pipelines/NIST/pipelines/bio4/metaphlan/merged/species_relab.txt",
    biobakery3="/Volumes/TBHD_share/valencia/pipelines/NIST/pipelines/bio3/metaphlan/merged/species_relab.txt",
    jams="/Volumes/TBHD_share/valencia/pipelines/NIST/pipelines/jams/beta_output/NIST_Relabund_PPM.xlsx",
    woltka="/Volumes/TBHD_share/valencia/pipelines/NIST/pipelines/woltka/classify",
    wgsa="/Volumes/TBHD_share/valencia/pipelines/NIST/pipelines/wgsa/outputs/TAXprofiles/TEDreadsTAX/reports",
    path=make_path("../pipelines/nist/"),
)


def make_data_list() -> List[MockCommData]:
    """Return a list of all the mock community data objects."""
    return [
        bmock12, camisim, tourlousse,
        amos_mixed, amos_hilo, hmpGut, nist]
