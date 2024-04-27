import heapq
import networkx as nx

# Define structures for graph nodes and edges
class Node:
    def __init__(self, id):
        self.id = id

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

# Initialize the graph with given nodes
def initializeGraph():
    nodes = [Node(i + 1) for i in range(40)]  # Changed to create only 5 nodes
    return nodes

# Add an edge to the graph
def addEdge(edges, source, destination, weight):
    edges.append(Edge(source, destination, weight))

# A* Algorithm
# def AStar(nodes, edges, start, end):
#     visited = [False] * len(nodes)
#     distances = [float('inf')] * len(nodes)
#     pq = [(0, start)]  
#     distances[start - 1] = 0

#     while pq:
#         distance, current = heapq.heappop(pq)
#         if current == end:
#             break

#         if visited[current - 1]:
#             continue

#         visited[current - 1] = True

#         for edge in edges:
#             if edge.source == current and not visited[edge.destination - 1]:
#                 newDistance = distance + edge.weight
#                 if newDistance < distances[edge.destination - 1]:
#                     distances[edge.destination - 1] = newDistance
#                     heapq.heappush(pq, (newDistance, edge.destination))

#     shortest_path = [end]
#     previous = end
#     while previous != start:
#         for edge in edges:
#             if edge.destination == previous and distances[edge.source - 1] == distances[previous - 1] - edge.weight:
#                 shortest_path.append(edge.source)
#                 previous = edge.source
#                 break
#     shortest_path.reverse()
#     return shortest_path
def AStar(nodes, edges, start, end):
    # Create a directed graph
    G = nx.DiGraph()

    # Add edges to the graph
    for edge in edges:
        G.add_edge(edge.source, edge.destination, weight=edge.weight)

    # Calculate the shortest path using A*
    shortest_path = nx.astar_path(G, start, end, weight='weight')

    return shortest_path
# Calculate fare based on distance
def calculateFare(distance):
    baseFare = 2.0  
    ratePerUnitDistance = 0.1  
    fare = baseFare + (distance * ratePerUnitDistance)
    return fare
