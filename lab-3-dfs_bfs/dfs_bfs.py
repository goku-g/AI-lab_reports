def DFS(graph, start, target):
    visited = []
    stack = []
    prev = dict()
    stack.append(start)

    while len(stack) > 0:
        popped = stack.pop()
        if popped not in visited:
            if popped == target:
                return (True, prev)
            visited.append(popped)

            for vertex in graph[popped]:
                if vertex not in visited and vertex not in stack:
                    stack.append(vertex)
                    prev[vertex] = popped
    return (False, prev)

def BFS(graph, start, target):
    visited = []
    queue = []
    prev = dict()
    queue.append(start)

    while len(queue) > 0:
        popped = queue.pop(0)
        if popped not in visited:
            if popped == target:
                return (True, prev)
            visited.append(popped)

            for vertex in graph[popped]:
                if vertex not in visited and vertex not in queue:
                    queue.append(vertex)
                    prev[vertex] = popped
    return (False, prev)

def draw_path(path, start, goal):
    map_ = goal
    temp = goal

    while path[temp] != start:
        map_ = path[temp] + "-->" + map_
        temp = path[temp]
    return start + "-->" + map_
        
graph = {
        'A': ['B', 'C'], 
        'B': ['D', 'E', 'A'], 
        'C': ['F', 'A'], 
        'D': ['G', 'B'], 
        'E': ['H', 'B'], 
        'F': ['C'], 
        'G': ['D'], 
        'H': ['E']
        }

start = 'B'
goal = 'G'

done, path = DFS(graph, start, goal)
print(done)
print(draw_path(path, start, goal))

done, path = BFS(graph, start, goal)
print(done)
print(draw_path(path, start, goal))