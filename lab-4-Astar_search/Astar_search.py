import numpy as np

g_index = 0
f_index = 1
prev = 2

def get_minimun(unvisited):
    fval = np.inf
    place = ""

    for city in unvisited.keys():
        if unvisited[city][1] < fval:
            fval = unvisited[city][1]
            place = city
    return place


def Astar(graph, start, goal):
    visited = {}
    unvisited = {}
    done = False

    for place in graph.keys():
        #                   g-score, f-score, previous
        unvisited[place] = [np.inf, np.inf, ""]
    
    unvisited[start] = [0, h[start], ""]

    while not done:
        if False:
            done = True
        else:
            current_node = get_minimun(unvisited)
            if current_node == goal:
                done = True
                visited[current_node] = unvisited[current_node]
            else:
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        g_score =  unvisited[current_node][g_index] + graph[current_node][neighbor]
                        
                        if g_score < unvisited[neighbor][g_index]:
                            unvisited[neighbor][g_index] = g_score
                            unvisited[neighbor][f_index] = g_score + h[neighbor]
                            unvisited[neighbor][prev] = current_node
                
                visited[current_node] = unvisited[current_node]
                del unvisited[current_node]
    
    return visited

graph = {
            "Biratnagar": {"Itahari":22, "Biratchowk":30, "Rangeli":25}, 
            "Itahari": {"Dharan":20, "Biratchowk":11, "Biratnagar":22},
            "Dharan": {"Itahari":20},
            "Rangeli": {"Kanepokhari":25, "Urlabari":40, "Biratnagar":25},
            "Biratchowk" : {"Kanepokhari":10, "Itahari":11, "Biratnagar":30},
            "Kanepokhari": {"Urlabari":12, "Rangeli":25, "Biratchowk":10},
            "Urlabari": {"Damak":6, "Kanepokhari":12, "Rangeli":40},
            "Damak": {"Urlabari":6}
        }
# heuristic function h(n)
h = {
            "Biratnagar": 46, 
            "Itahari": 39,
            "Dharan": 41,
            "Rangeli": 28,
            "Biratchowk" : 29,
            "Kanepokhari": 17,
            "Urlabari": 6,
            "Damak": 0
         }

def make_map(dict, goal):
    path = goal
    temp = goal
    while dict[temp][prev] != "":
        path = dict[temp][prev] + "-->" + path
        temp = dict[temp][prev]
    
    return path

if __name__ == "__main__":

    start = "Biratnagar"
    goal = "Damak"

    visit_node = Astar(graph, start, goal)

    print(make_map(visit_node, goal))