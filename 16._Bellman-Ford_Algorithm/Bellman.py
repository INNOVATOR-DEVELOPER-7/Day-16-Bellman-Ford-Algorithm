def bellman_ford(graph, vertices, start_node):
    # Initialize distances from start node to all other nodes as infinity
    distances = {vertex: float('infinity') for vertex in vertices}
    distances[start_node] = 0

    # Relax all edges |V| - 1 times (where |V| is the number of vertices)
    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
            print("Graph contains a negative-weight cycle")
            return None

    return distances

# Get the number of vertices from the user
num_vertices = int(input("Enter the number of vertices: "))
vertices = []
for i in range(num_vertices):
    vertex = input(f"Enter the name of vertex {i+1}: ")
    vertices.append(vertex)

# Get the edges of the graph from the user
num_edges = int(input("Enter the number of edges: "))
graph = []
print("Enter each edge in the format 'source destination weight':")
for i in range(num_edges):
    edge = input().split()
    graph.append((edge[0], edge[1], int(edge[2])))

# Get the starting node from the user
start_node = input("Enter the starting node: ")

# Perform Bellman-Ford algorithm
distances = bellman_ford(graph, vertices, start_node)

# Print the shortest distances from the start node to all other nodes
if distances:
    print("Shortest distances from node", start_node, ":")
    for vertex in distances:
        print(f"Distance to {vertex}: {distances[vertex]}")
