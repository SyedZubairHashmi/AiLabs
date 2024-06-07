# from itertools import permutations

# def calculate_distance(route, distance_matrix):
#     """
#     Calculate the total distance of the given route.
    
#     Parameters:
#     - route: a list representing the order in which the cities are visited.
#     - distance_matrix: a 2D list where distance_matrix[i][j] represents the distance from city i to city j.
    
#     Returns:
#     - Total distance of the route.
#     """
#     total_distance = 0
#     for i in range(len(route) - 1):
#         total_distance += distance_matrix[route[i]][route[i + 1]]
#     total_distance += distance_matrix[route[-1]][route[0]]  # Return to the starting city
#     return total_distance

# def traveling_salesman(distance_matrix):
#     """
#     Solves the TSP using a brute-force method.
    
#     Parameters:
#     - distance_matrix: a 2D list where distance_matrix[i][j] represents the distance from city i to city j.
    
#     Returns:
#     - The shortest route and its total distance.
#     """
#     num_cities = len(distance_matrix)
#     all_routes = permutations(range(num_cities))
#     shortest_route = None
#     min_distance = float('inf')
    
#     for route in all_routes:
#         current_distance = calculate_distance(route, distance_matrix)
#         if current_distance < min_distance:
#             min_distance = current_distance
#             shortest_route = route
    
#     return shortest_route, min_distance

# # Example usage
# distance_matrix = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# shortest_route, min_distance = traveling_salesman(distance_matrix)
# print(f"The shortest route is: {shortest_route}")
# print(f"The minimum distance is: {min_distance}")


# part b
def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi problem and print the moves.
    
    Parameters:
    - n: Number of disks
    - source: The initial rod
    - auxiliary: The auxiliary rod
    - target: The target rod
    """
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {target}")
        return
    # Move n-1 disks from source to auxiliary, so they are out of the way
    tower_of_hanoi(n - 1, source, target, auxiliary)
    # Move the nth disk from source to target
    print(f"Move disk {n} from rod {source} to rod {target}")
    # Move the n-1 disks that were left on auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'B', 'C')
