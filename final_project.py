# Isaiah Lugo
# CSM IV - Algorithms
# Final Project


import heapq

# -------------------------------
# Algorithm 1: Lowest Cost Delivery Between Two Locations
# Implements Dijkstra's Algorithm
# -------------------------------

def algorithm_1(graph, start, end):
    """
    Finds the lowest cost path from start to end using Dijkstra's algorithm.
    Parameters:
        graph (dict): Weighted graph represented as adjacency list.
        start (str): Starting node.
        end (str): Destination node.
    Returns:
        tuple: (list of nodes representing the shortest path, total cost)
    """
    queue = [(0, start, [start])]  # Min-heap priority queue storing (cost, current_node, path)
    visited = set()  # Track visited nodes to prevent reprocessing

    while queue:
        cost, current, path = heapq.heappop(queue)  # Get node with lowest cost so far

        if current == end:
            return path, cost  # Found the shortest path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):  # Explore all connected nodes
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None, float("inf")  # Return no path found if unreachable


# -------------------------------
# Algorithm 2: Best Path from the Hub (Minimum Spanning Tree)
# Implements Prim's Algorithm
# -------------------------------

def algorithm_2(graph, hub):
    """
    Builds a Minimum Spanning Tree (MST) from the hub using Prim's Algorithm.
    Parameters:
        graph (dict): Weighted graph.
        hub (str): Starting hub node.
    Returns:
        tuple: (list of edges in MST, total cost of MST)
    """
    visited = set([hub])  # Initialize visited set with hub
    edges = []  # Priority queue for edges to be explored
    mst = []  # Store the MST edges
    total_cost = 0  # Total cost of the MST

    # Load initial edges from the hub
    for neighbor, weight in graph.get(hub, []):
        heapq.heappush(edges, (weight, hub, neighbor))

    while edges:
        weight, frm, to = heapq.heappop(edges)  # Get edge with minimum weight
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))  # Add edge to MST
            total_cost += weight  # Add weight to total cost

            for neighbor, w in graph.get(to, []):  # Add new edges from visited node
                if neighbor not in visited:
                    heapq.heappush(edges, (w, to, neighbor))

    return mst, total_cost


# -------------------------------
# Algorithm 3: Dynamic Network Changes
# Removes and Adds Edges Before Running MST
# -------------------------------

def algorithm_3(graph, hub, remove_edges, add_edges):
    """
    Modifies the graph based on removals and additions, then runs MST.
    Parameters:
        graph (dict): Original graph (adjacency list).
        hub (str): Starting hub node.
        remove_edges (list): List of edges to remove in the format ["A-B"].
        add_edges (list): List of edges to add in the format [("A", "B", weight)].
    Returns:
        tuple: (list of edges in new MST, total cost)
    """
    # Make a copy to avoid modifying the original graph
    new_graph = {node: neighbors[:] for node, neighbors in graph.items()}

    # Remove specified edges from the graph
    for edge in remove_edges:
        node1, node2 = edge.split('-')
        new_graph[node1] = [pair for pair in new_graph[node1] if pair[0] != node2]
        new_graph[node2] = [pair for pair in new_graph[node2] if pair[0] != node1]

    # Add new edges to the graph
    for node1, node2, weight in add_edges:
        new_graph.setdefault(node1, []).append((node2, weight))
        new_graph.setdefault(node2, []).append((node1, weight))

    # Re-run MST on the updated graph
    return algorithm_2(new_graph, hub)


# -------------------------------
# Example Graph and Test Calls
# -------------------------------

if __name__ == "__main__":
    example_graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)]
    }

    # Test Algorithm 1 - Dijkstra's shortest path
    print("Algorithm 1:")
    print("A to E:", algorithm_1(example_graph, "A", "E"))
    print("A to B:", algorithm_1(example_graph, "A", "B"))

    # Test Algorithm 2 - Prim's MST from hub A
    print("\nAlgorithm 2:")
    mst, cost = algorithm_2(example_graph, "A")
    print("MST:", mst)
    print("Cost:", cost)

    # Test Algorithm 3 - Update graph and run MST
    print("\nAlgorithm 3:")
    updated_mst, updated_cost = algorithm_3(example_graph, "A", ["C-E"], [("B", "E", 3)])
    print("Updated MST:", updated_mst)
    print("Updated Cost:", updated_cost)
