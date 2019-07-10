import numpy as np

vertices = list('ABCDE')
# vertices = ['Highgarden', "King's Landing", 'Riverrun', 'Pyke', 'The Trident', 'Winterfell']
# start = 'Highgarden'
# goal = 'Winterfell'
start = 'A'
goal = 'C'

distances = {v: np.infty for v in vertices}
distances[start] = 0

previous_vertices = {v: None for v in vertices}
previous_vertices[start] = start

unvisited, visited = vertices, []


graph = {'A': {'B': 2, 'D': 4}, 
         'B': {'A': 2, 'D': 1, 'E': 11, 'C': 38},
         'C': {'B': 38, 'E': 20},
         'D': {'A': 4, 'B': 1, 'E': 9},
         'E': {'D': 9, 'B': 11, 'C': 20}
        }

# graph = {'Highgarden': {"King's Landing": 8, 'Riverrun': 10, 'Pyke': 14}, 
#          "King's Landing": {'Highgarden': 8, 'Riverrun': 25, 'The Trident': 5},
#          'Riverrun': {'Highgarden': 10, "King's Landing": 25, 'Pyke': 3, 'The Trident': 2},
#          'The Trident': {"King's Landing": 5, 'Riverrun': 2, 'Winterfell': 10},
#          'Pyke': {'Highgarden': 14, 'Riverrun': 3, 'Winterfell': 18},
#          'Winterfell': {'Pyke': 18, 'The Trident': 10}
#         }


def get_shortest_distances(start):
    while len(unvisited) > 0:
        current_vertex = min(unvisited, key=distances.get)
        unvisited.remove(current_vertex)
        visited.append(current_vertex)

        for (vertex, edge) in graph[current_vertex].items():
            if vertex in unvisited:
                if edge + distances[current_vertex] < distances[vertex] or distances[vertex] == np.infty:
                    distances[vertex] = edge + distances[current_vertex]
                    previous_vertices[vertex] = current_vertex
    
def get_shortest_path(start, goal):
    result = goal
    path = [result]
    while result != start:
        result = previous_vertices[result]
        path.append(result)
    
    return path[::-1]



get_shortest_distances(start)
print(distances)
print(get_shortest_path(start, goal))
