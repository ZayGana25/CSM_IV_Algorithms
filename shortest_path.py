# Isaiah Lugo
# CSM IV - Algorithms
# Week 9 - Shortest Path


import sys

class Graph:
    def __init__(self, size):
        # Step 2:
        self.size = size

        self.adjacency_matrix = [[0 for _ in range(size)] for _ in range(size)]

        self.node_data = ["" for _ in range(size)]
    
    def add_edge(self, node1, node2, weight):
        # Step 3: 
        self.adjacency_matrix[node1][node2] = weight
        self.adjacency_matrix[node2][node1] = weight  
    
    def add_node_data(self, node, data):

        self.node_data[node] = data
    
    def dijkstra(self, start_node_data):
        # Step 4: 
        start_node = self.node_data.index(start_node_data)

        distances = [sys.maxsize] * self.size

        distances[start_node] = 0
        
        visited = [False] * self.size
        
        for _ in range(self.size):
            # Step 5: 
            min_distance = sys.maxsize
            min_index = -1
            
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    min_index = i
            
            if min_index == -1:
                break
            
            visited[min_index] = True
            
            for neighbor in range(self.size):
                if (self.adjacency_matrix[min_index][neighbor] > 0 and
                        not visited[neighbor] and
                        distances[min_index] + self.adjacency_matrix[min_index][neighbor] < distances[neighbor]):

                    distances[neighbor] = distances[min_index] + self.adjacency_matrix[min_index][neighbor]
        
        return distances

# Example Inputs and Outputs
test_1 = Graph(5)
test_1.add_node_data(0, "A") 
test_1.add_node_data(1, "B")
test_1.add_node_data(2, "C") 
test_1.add_node_data(3, "D") 
test_1.add_node_data(4, "E")
test_1.add_edge(0, 1, 2) 
test_1.add_edge(0, 2, 4) 
test_1.add_edge(1, 2, 1) 
test_1.add_edge(1, 3, 7) 
test_1.add_edge(2, 3, 3) 
test_1.add_edge(3, 4, 1) 
test_1.add_edge(0, 4, 8)

print(test_1.adjacency_matrix) # [[0, 2, 4, 0, 8], [2, 0, 1, 7, 0], [4, 1, 0, 3, 0], [0, 7, 3, 0, 1], [8, 0, 0, 1, 0]]
print(test_1.node_data) # ["A", "B", "C", "D", "E"]
print(test_1.dijkstra("A")) # [0, 2, 3, 6, 7]
print(test_1.dijkstra("C")) # [3, 1, 0, 3, 4]
