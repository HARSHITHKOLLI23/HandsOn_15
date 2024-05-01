import heapq
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

#Dijkstra's algorithm to find shortest paths
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous = {node: None for node in graph}

    while pq:

        cur_distance, cur_node = heapq.heappop(pq)
     
        if cur_distance > distances[cur_node]:
            continue
       
        for neighbor, weight in graph[cur_node].items():
            distance = cur_distance + weight
           
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = cur_node
                
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


def print_graph(graph):
    print("Graph:")
    for u in graph:
        for v, weight in graph[u].items():
            print(f"{u} -> {v} : {weight}")
    print()

# Print shortest paths and previous nodes
def print_shortest_path(graph, start_node, distances, previous):
    print("Shortest Paths from", start_node + ":")
    for node, distance in distances.items():
        print(f"Shortest path from {start_node} to {node}: {distance}")
    print("\nPrevious nodes:")
    for node, prev_node in previous.items():
        print(node + ":", prev_node)
    print()

# Construct edges of the shortest path graph
def construct_shortest_path_edges(graph, previous):
    shortest_path_edges = []
    for node in previous:
        if previous[node] is not None:
            shortest_path_edges.append(Edge(previous[node], node, graph[previous[node]][node]))
    return shortest_path_edges

# Example graph
graph = {
    'S': {'T': 10, 'Y': 5, 'Z': 7},
    'T': {'X': 1, 'Y': 2},
    'X': {'Z': 4},
    'Y': {'Z': 2, 'T': 3, 'X': 9},
    'Z': {'S': 7, 'X': 6}
}

start_node = 'S'

distances, previous = dijkstra(graph, start_node)
print_graph(graph)
print_shortest_path(graph, start_node, distances, previous)

shortest_path_edges = construct_shortest_path_edges(graph, previous)
print("Shortest Path Graph:")
for edge in shortest_path_edges:
    print(f"{edge.start} -> {edge.end} : {edge.weight}")
