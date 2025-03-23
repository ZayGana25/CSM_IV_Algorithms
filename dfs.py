# Isaiah Lugo
# CSM IV - Algorithms
# Week 8 - Depth First Search


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

    def dfs(self, start_node):
        stack = [start_node]
        visited = [False] * self.size
        order = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                order.append(node)
                for neighbor, _ in reversed(self.adjacency_list[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return order

# Example inputs and expected outputs
g = Graph(5)
g.add_node_data(0, "Node 1")
g.add_node_data(1, "Node 2")
g.add_node_data(2, "Node 3")
g.add_node_data(3, "Node 4")
g.add_node_data(4, "Node 5")
print(g.adjacency_list)  # {0: [], 1: [], 2: [], 3: [], 4: []}
print(g.node_data)  # ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5']
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(1, 2, 2)
print(g.adjacency_list)  # {0: [(1, 2), (2, 2), (3, 2)], 1: [(0, 2), (4, 2), (2, 2)], 2: [(0, 2), (1, 2)], 3: [(0, 2)], 4: [(1, 2)]}
print(g.dfs(0))  # [0, 1, 4, 2, 3]
print(g.dfs(4))  # [4, 1, 0, 2, 3]
print(g.dfs(2))  # [2, 0, 1, 4, 3]
