# Import necessary modules
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import initializeGraph, addEdge, AStar, calculateFare
from django.shortcuts import render
from django.http import HttpResponse

mp = [(1,"Bus Stand"),(2,"Knowledge Tree"),(3,"Office Buildings"),(4,"Shamiyana"),(5,"Profs Apartment"),(6,"Jodhpur Club"),(7,"Sports Complex"),(8,"Temple"),(9,"Chemical/Material Department"),(10,"Basics Lab"),(11,"CSE Department"),(12,"Bio Department"),(13,"Chemistry Department"),(14,"Mechanical Department"),(15,"Civil Department"),(16,"Electrical Department"),(17,"Phy Department"),(18,"LHB"),(19,"SME"),(20,"Maths Department"),(21,"Snacks Shop 1"),(22,"Snacks Shop 2"),(23,"AIDE"),(24,"Main Gate"),(25,"NIFT Gate"),(26,"Y4"),(27,"Y3"),(28,"B1"),(29,"B2"),(30,"B5"),(31,"I2"),(32,"I3"),(33,"New Mess"),(34,"Old Mess"),(35,"Laundry"),(36,"Kendriya Bhandar"),(37,"Tinkering Lab"),(38,"Barber Shop"),(39,"Stationery"),(40,"Library")]

def final_Res(shortest_path):
    res = ""
    for i in shortest_path:
        res += mp[int(i)-1][1] + "->"
    res = res[:-2]  # Removed the extra "->" at the end
    return res

@csrf_exempt
def request_ride(request):
    if request.method == 'POST':
        # Parse POST data
        start = int(request.POST.get('start'))
        end = int(request.POST.get('end'))
        print(start,"output for start")
        
        # Initialize graph and edges
        nodes = initializeGraph()
        edges = []
        
        # Define edges
        addEdge(edges, 1, 2, 0.65)  # Bus Stand to Knowledge Tree
        addEdge(edges, 2, 3, 0.4)   # Knowledge Tree to Office Buildings
        addEdge(edges, 3, 4, 0.75)  # Office Buildings to Shamiyana
        addEdge(edges, 4, 5, 0.6)   # Shamiyana to Profs Apartment
        addEdge(edges, 5, 6, 0.75)  # Profs Apartment to Jodhpur Club
        addEdge(edges, 6, 7, 1.1)   # Jodhpur Club to Sports Complex
        addEdge(edges, 7, 8, 2.7)   # Sports Complex to Temple
        addEdge(edges, 8, 9, 1.1)   # Temple to Chemical/Material Department
        addEdge(edges, 9, 10, 0.5)  # Chemical/Material Department to Basics Lab
        addEdge(edges, 10, 11, 0.5) # Basics Lab to CSE Department
        addEdge(edges, 11, 12, 0.6) # CSE Department to Bio Department
        addEdge(edges, 12, 13, 0.6) # Bio Department to Chemistry Department
        addEdge(edges, 13, 14, 1.0) # Chemistry Department to Mechanical Department
        addEdge(edges, 14, 15, 0.9) # Mechanical Department to Civil Department
        addEdge(edges, 15, 16, 1.0) # Civil Department to Electrical Department
        addEdge(edges, 16, 17, 1.1) # Electrical Department to PHY Department
        addEdge(edges, 17, 18, 0.7) # PHY Department to LHB
        addEdge(edges, 18, 19, 1.1) # LHB to SME Department
        addEdge(edges, 19, 20, 1.2) # SME Department to Maths Department
        addEdge(edges, 20, 21, 0.9) # Maths Department to Snacks Shop 1
        addEdge(edges, 21, 22, 0.5) # Snacks Shop 1 to Snacks Shop 2
        addEdge(edges, 22, 23, 0.4) # Snacks Shop 2 to AIDE
        addEdge(edges, 23, 24, 0.8) # AIDE to Main Gate
        addEdge(edges, 24, 25, 2.3) # Main Gate to NIFT Gate
        addEdge(edges, 25, 26, 0.95) # NIFT Gate to Y4
        addEdge(edges, 26, 27, 0.95) # Y4 to Y3
        addEdge(edges, 27, 28, 0.7) # Y3 to B1
        addEdge(edges, 28, 29, 0.7) # B1 to B2
        addEdge(edges, 29, 30, 0.6) # B2 to B5
        addEdge(edges, 30, 31, 0.6) # B5 to I2
        addEdge(edges, 31, 32, 0.5) # I2 to I3
        addEdge(edges, 32, 33, 0.6) # I3 to New Mess
        addEdge(edges, 33, 34, 0.5) # New Mess to Old Mess
        addEdge(edges, 34, 35, 0.9) # Old Mess to Laundry
        addEdge(edges, 35, 36, 0.6) # Laundry to Kendriya Bhandar
        addEdge(edges, 36, 37, 0.7) # Kendriya Bhandar to Tinkering Lab
        addEdge(edges, 37, 38, 0.8) # Tinkering Lab to Barber Shop
        addEdge(edges, 38, 39, 0.9) # Barber Shop to Stationery
        addEdge(edges, 39, 40, 0.4) # Stationery to Library
        
        # Find shortest path
        shortest_path = AStar(nodes, edges, start, end)
        print(shortest_path, "this is the short")
        
        if shortest_path:
            # Calculate distance and fare
            distance = sum(edge.weight for edge in edges if edge.source in shortest_path and edge.destination in shortest_path)
            fare = calculateFare(distance)
            
            # Construct result
            result = {
                'shortestPath': final_Res(shortest_path),
                'fare': fare,
            }
            print(distance)
            print(fare)
            print(result)
        else:
            result = {
                # 'message': f"No path found between nodes {start} and {end}"
            }
            print(result)

        # Return the result as a JSON response
        return JsonResponse(result)

def home(request):
    return render(request, 'interface.html')

def ride_sharing_interface(request):
    return render(request, 'interface.html')
