import sys

import networkx
from rapdevpy import networkx_lib


def generate_systems_within_distance_list(max_distance: int):
    graph = networkx_lib.read_graph_edges("eve_tools/system_map/data/null-jump-edgelist.csv")
    with open("output.csv", "w") as output:
        with open("eve_tools/system_map/data/arc-jove-null-systems.csv", "r") as joves:
            for jove in joves:
                vertex = str(jove.strip())
                descendants = networkx_lib.get_graph_vertices_up_to_distance(
                    graph, vertex, max_distance
                )

                output.write(",".join([vertex] + descendants) + "\n")


def generate_anomic_path_list():
    graph = networkx_lib.read_graph_edges("eve_tools/system_map/data/null-jump-edgelist.csv")
    shortest_paths = []
    with open("eve_tools/system_map/data/anomic-origin-target.csv", "r") as origin_target_pairs:
        for origin_target_pair in origin_target_pairs:
            origin, target = origin_target_pair.split(" ")
            shortest_path = networkx.shortest_path(graph, str(origin.strip()), str(target.strip()))
            distance = len(shortest_path) - 1
            shortest_path.extend(["-" for _ in range(8 - len(shortest_path))])
            shortest_path.append(str(distance))
            shortest_paths.append(shortest_path)
    shortest_paths.sort()

    with open("output.csv", "w") as output:
        for shortest_path in shortest_paths:
            output.write(",".join(shortest_path) + "\n")


def main(args):
    """main() will be run if you run this script directly"""
    generate_anomic_path_list()


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
