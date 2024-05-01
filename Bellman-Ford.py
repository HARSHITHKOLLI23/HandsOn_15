class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

#distances and predecessors for vertices
def initialize_single_source(vertices, start):
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    predecessors = {v: None for v in vertices}
    return distances, predecessors

# Bellman-Ford algorithm to find shortest paths
def bellman_ford_algorithm(vertices, edges, start):
    distances, predecessors = initialize_single_source(vertices, start)
    for _ in range(len(vertices) - 1):
        for edge in edges:
            relax(edge.start, edge.end, edge.weight, distances, predecessors)
    for edge in edges:
        if distances[edge.end] > distances[edge.start] + edge.weight:
            return False
    return distances, predecessors

# Relaxation step to update distances and predecessors
def relax(u, v, weight, distances, predecessors):
    if distances[v] > distances[u] + weight:
        distances[v] = distances[u] + weight
        predecessors[v] = u

# Print the original graph
def print_graph(vertices, edges):
    print("Original Graph:")
    for edge in edges:
        print(edge.start, "->", edge.end, ":", edge.weight)
    print()

# Print shortest distances and their predecessors
def print_shortest_distances(distances, predecessors, start):
    print("Shortest distances from", start)
    for vertex, distance in distances.items():
        print("Vertex:", vertex, "Distance:", distance, "Predecessor:", predecessors[vertex])
    print()

#graph of shortest distances
def construct_shortest_distance_graph(vertices, edges, distances, predecessors):
    shortest_distance_edges = []
    for vertex in vertices:
        predecessor = predecessors[vertex]
        if predecessor is not None:
            shortest_distance_edges.append(Edge(predecessor, vertex, distances[vertex]))
    return shortest_distance_edges

# Print the graph of shortest distances
def print_shortest_distance_graph(shortest_distance_edges):
    print("Shortest Distance Graph:")
    for edge in shortest_distance_edges:
        print(edge.start, "->", edge.end, ":", edge.weight)
    print()

# Example usage (Figure 24.4 from Page 652):
vertices = ['s', 't', 'x', 'y', 'z']
edges = [
    Edge('s', 't', 6),
    Edge('s', 'y', 7),
    Edge('t', 'x', 5),
    Edge('t', 'y', 8),
    Edge('t', 'z', -4),
    Edge('x', 't', -2),
    Edge('y', 'x', -3),
    Edge('y', 'z', 9),
    Edge('z', 'x', 7),
    Edge('z', 's', 2)
]
start = 's'


print_graph(vertices, edges)

result = bellman_ford_algorithm(vertices, edges, start)
if result:
    distances, predecessors = result
    print_shortest_distances(distances, predecessors, start)
    shortest_distance_edges = construct_shortest_distance_graph(vertices, edges, distances, predecessors)
    print_shortest_distance_graph(shortest_distance_edges)
else:
    print("Negative cycle detected")
