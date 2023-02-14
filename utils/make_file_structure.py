import os


def make_file_structure(root_dir: str):
    """This function will make a file structure for the data."""
    sources = ["amos", "bmock12", "camisimGI", "nist", "hmp", "tourlousse"]
    amos_subdirs = ["hilo", "mixed"]
    hmp_subdirs = ["gut", "tongue"]

    pipelines = ["biobakery3", "biobakery4",
                 "jams", "jams202212", "wgsa2", "woltka"]

    for source in sources:
        if source == "amos":
            for subdir in amos_subdirs:
                for pipeline in pipelines:
                    output = os.path.join(root_dir, source, subdir, pipeline)
                    os.makedirs(output)
        elif source == "hmp":
            for subdir in hmp_subdirs:
                for pipeline in pipelines:
                    output = os.path.join(root_dir, source, subdir, pipeline)
                    os.makedirs(output)
        else:
            for pipeline in pipelines:
                output = os.path.join(root_dir, source, pipeline)
                os.makedirs(output)


if __name__ == "__main__":
    this_file = os.path.dirname(__file__)
    make_file_structure(os.path.join(this_file, "../pipelines"))
