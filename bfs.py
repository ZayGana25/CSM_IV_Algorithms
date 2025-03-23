# Isaiah Lugo
# CSM IV - Algorithms
# Week 7 - Breadth First Search

class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = {i: [] for i in range(size)}
        self.node_data = ["" for _ in range(size)]

    def add_edge(self, node1, node2, weight):
        self.adjacency_list[node1].append((node2, weight))
        self.adjacency_list[node2].append((node1, weight))

    def add_node_data(self, node, data):
        self.node_data[node] = data

    def bfs(self, start_node):
        queue = [start_node]
        visited = [False] * self.size
        order = []
        
        visited[start_node] = True
        
        while queue:
            current = queue.pop(0)
            order.append(current)
            
            for neighbor, _ in self.adjacency_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return order

# Example Usage
g = Graph(5)
g.add_node_data(0, "A")
g.add_node_data(1, "B")
g.add_node_data(2, "C")
g.add_node_data(3, "D")
g.add_node_data(4, "E")

print(g.adjacency_list)  # Initially empty adjacency list
print(g.node_data)  # ['A', 'B', 'C', 'D', 'E']

g.add_edge(0, 1, 2)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(1, 2, 2)

print(g.adjacency_list)
print(g.bfs(0))  # Expected: [0, 1, 2, 3, 4]
print(g.bfs(1))  # Expected: [1, 0, 4, 2, 3]
print(g.bfs(2))  # Expected: [2, 0, 1, 3, 4]
