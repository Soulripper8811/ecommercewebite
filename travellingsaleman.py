from itertools import permutations

def tsp(distance_matrix):
    n = len(distance_matrix)
    routes = permutations(range(n))  

    return min((sum(distance_matrix[route[i]][route[(i+1)%n]] for i in range(n)),route) for route in routes)


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


min_distance, route = tsp(distance_matrix)
print("Shortest route:", route, "with distance:", min_distance)
