from collections import deque

def bfs(graph, visited, queue):
    last_count = 0
    last_nodes = []
    while queue:
        node, count = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                if count + 1 > last_count:
                    last_count = count + 1
                    last_nodes = [next_node]
                elif count + 1 == last_count:
                    last_nodes.append(next_node)
                queue.append([next_node, last_count])
    return len(last_nodes)
    
def set_graph(graph, edge):
    for vertex in edge:
        if vertex[0] in graph:
            graph[vertex[0]].append(vertex[1])
        else:
            graph[vertex[0]] = [vertex[1]]
        if vertex[1] in graph:
            graph[vertex[1]].append(vertex[0])
        else:
            graph[vertex[1]] = [vertex[0]]

def solution(n, edge):
    answer = 0
    
    visited = [False for i in range(n + 1)]
    graph = dict()
    set_graph(graph, edge)
    visited[1] = True
    return bfs(graph, visited, deque([[1, 0]]))
    