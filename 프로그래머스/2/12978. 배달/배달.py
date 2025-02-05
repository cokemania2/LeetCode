def dfs_recursive(graph, road_dict, check, visited, node, length_sum, K):
    result = set()
    result.add(node)
    check[node - 1] = length_sum
    for neighbor in graph[node]:
        length = road_dict[tuple(sorted([node, neighbor]))]
        if length_sum + length > K or visited[neighbor - 1] or length_sum + length > check[neighbor - 1]:
            continue
        visited[neighbor - 1] = True
        result |=  dfs_recursive(graph, road_dict, check, visited, neighbor, length_sum + length, K)
        visited[neighbor - 1] = False

    return result


def solution(N, road, K):
    answer = 0
    graph = dict()
    road_dict = dict()
    
    for a, b, c in road:
        a, b = sorted([a,b])
        if (a,b) not in road_dict:
            road_dict[(a,b)] = c
        else:
            road_dict[(a,b)] = min(road_dict[(a,b)], c)
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    
    visited = [False for _ in range(N)]
    visited[0] = True
    check = [float('inf') for _ in range(N)]
    return len(dfs_recursive(graph, road_dict, check, visited, 1, 0, K))