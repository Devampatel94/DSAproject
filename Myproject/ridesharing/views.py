# Import necessary modules
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import initializeGraph, addEdge, AStar, calculateFare
from django.shortcuts import render
from django.http import HttpResponse

# Your existing view function
@csrf_exempt
def request_ride(request):
    if request.method == 'POST':
        # Parse POST data
        start = int(request.POST.get('start'))
        end = int(request.POST.get('end'))

        # Initialize graph and edges
        nodes = initializeGraph()
        edges = []
        addEdge(edges, 1, 2, 10.0)
        addEdge(edges, 1, 3, 15.0)
        addEdge(edges, 2, 4, 8.0)
        addEdge(edges, 3, 4, 12.0)
        addEdge(edges, 3, 5, 18.0)
        addEdge(edges, 4, 5, 9.0)

        # Calculate shortest path and fare
        shortest_path = AStar(nodes, edges, start, end)
        if shortest_path:
            distance = sum(edge.weight for edge in edges if edge.source in shortest_path and edge.destination in shortest_path)
            fare = calculateFare(distance)
            result = f"Shortest path from node {start} to node {end}: {' <- '.join(map(str, shortest_path))}. Estimated fare for the ride: ${fare:.2f}"
        else:
            result = f"No path found between nodes {start} and {end}"

        # Return the result as a plain HTTP response
        return HttpResponse(result)
def home(request):
    return render(request, 'interface.html')

def ride_sharing_interface(request):
    return render(request, 'interface.html')