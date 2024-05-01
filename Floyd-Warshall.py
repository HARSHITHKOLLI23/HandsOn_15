# Define a class representing edges in a graph
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

# Implement the Floyd-Warshall algorithm for finding shortest paths
def floyd_warshall_algorithm(graph):
    # Initialize distance matrix
    distance = {u: {v: float('inf') if u != v else 0 for v in graph} for u in graph}

    # Initialize distance matrix with direct edges
    for u in graph:
        for v in graph[u]:
            distance[u][v] = graph[u][v]

    # Calculate shortest paths
    for k in graph:
        for i in graph:
            for j in graph:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# Print the original graph
def print_graph(graph):
    print("Graph:")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {graph[u][v]}")
    print()

# Print shortest paths
def print_shortest_paths(all_pairs_shortest_paths):
    print("Shortest Paths:")
    for u in all_pairs_shortest_paths:
        for v in all_pairs_shortest_paths[u]:
            print(f"Shortest path from {u} to {v}: {all_pairs_shortest_paths[u][v]}")
        print()

# Construct a graph from shortest paths
def construct_graph_from_shortest_paths(graph, all_pairs_shortest_paths):
    shortest_path_edges = []
    for u in graph:
        for v in graph[u]:
            shortest_path_edges.append(Edge(u, v, all_pairs_shortest_paths[u][v]))
    return shortest_path_edges

# Print the graph of shortest paths
def print_shortest_path_graph(shortest_path_edges):
    print("Shortest Path Graph:")
    for edge in shortest_path_edges:
        print(f"{edge.start} -> {edge.end} : {edge.weight}")
    print()

# Example graph (Figure 25.1 from Page 690)
graph = {
    '1': {'2': 3, '3': 8, '5': -4},
    '2': {'5': 7, '4': 1},
    '3': {'2': 4},
    '4': {'3': -5, '1': 2},
    '5': {'4': 6}
}

# Print the original graph
print_graph(graph)

# Execute the Floyd-Warshall algorithm and print results
all_pairs_shortest_paths = floyd_warshall_algorithm(graph)
print_shortest_paths(all_pairs_shortest_paths)

# Construct and print the graph of shortest paths
shortest_path_edges = construct_graph_from_shortest_paths(graph, all_pairs_shortest_paths)
print_shortest_path_graph(shortest_path_edges)
