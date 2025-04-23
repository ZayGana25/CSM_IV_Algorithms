# Isaiah Lugo
# CSM IV - Algorithms
# Week 10 - Minimum Spanning Tree

# When running the code, the output for Prim's MST is [(0, 3, 5), (3, 2, 4), (3, 4, 7), (0, 1, 10)]
# which is different from the expected output in the comments. The expected output for Kruskal's MST is
# [(2, 3, 4), (0, 3, 5), (3, 4, 7), (0, 1, 10)] which is the same as the output from the code. I 
# attempted to debug the code but was unable to find the issue. I consulted with ChatGPT as well to 
# find any errors that lied within, but kept receiving the same result and output. I believe the expected
# value for Prims MST is incorrect and the output from the code is correct, but would love confirmation.

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # Since it's an undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def prims_algorithm(self, start_node_data):
        # Find the index of the start node
        start_node = self.vertex_data.index(start_node_data)

        visited = [False] * self.size  # Keep track of visited nodes
        mst = []
        visited[start_node] = True  # Start from the given node

        for _ in range(self.size - 1):  # MST has (V - 1) edges
            min_edge = None
            min_weight = float('inf')

            # Find the smallest edge that connects a visited node to an unvisited node
            for u in range(self.size):
                if visited[u]:  # Look for edges from visited nodes
                    for v in range(self.size):
                        if not visited[v] and self.adj_matrix[u][v] > 0:  # Valid edge
                            if self.adj_matrix[u][v] < min_weight:
                                min_weight = self.adj_matrix[u][v]
                                min_edge = (u, v, min_weight)

            if min_edge:
                u, v, weight = min_edge
                mst.append(min_edge)
                visited[v] = True  # Mark the new node as visited

        return mst

    def kruskals_algorithm(self):
        edges = []
        for u in range(self.size):
            for v in range(u + 1, self.size):  # Avoid duplicate edges
                if self.adj_matrix[u][v] > 0:
                    edges.append((self.adj_matrix[u][v], u, v))

        edges.sort()  # Sort edges by weight

        parent = list(range(self.size))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v

        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):  # Ensure no cycle is formed
                union(u, v)
                mst.append((u, v, weight))

        return mst


# Create a graph with 5 vertices 
graph = Graph(5)

graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 7)

graph.add_vertex_data(0, 'A')
graph.add_vertex_data(1, 'B')
graph.add_vertex_data(2, 'C')
graph.add_vertex_data(3, 'D')
graph.add_vertex_data(4, 'E')

print("\n Outputs: \n")
# Call Prim's algorithm starting from node 'A'
mst_prim = graph.prims_algorithm('A')
print("Prim's MST:", mst_prim) # Expected output: [(0, 3, 5), (3, 2, 4), (2, 0, 6), (3, 4, 7)]

# Call Kruskal's algorithm to find the MST
mst_kruskal = graph.kruskals_algorithm()
print("Kruskal's MST:", mst_kruskal) # Expected output: [(2, 3, 4), (0, 3, 5), (3, 4, 7), (0, 1, 10)]

print()

