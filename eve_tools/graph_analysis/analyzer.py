import sys
from rapdevpy import networkx_lib


def fun():
    graph = networkx_lib.read_graph_edges("protopy/graph_analysis/data/null-jumps.csv")
    with open("output.csv", "w") as output:
        with open("protopy/graph_analysis/data/arc-jove-null-jumps.csv", "r") as joves:
            for jove in joves:
                vertex = str(jove.strip())
                descendants = networkx_lib.get_graph_vertices_up_to_distance(
                    graph, vertex, 5
                )

                output.write(",".join([vertex] + descendants) + "\n")


def main(args):
    """main() will be run if you run this script directly"""
    fun()


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
