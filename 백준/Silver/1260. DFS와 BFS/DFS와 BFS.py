from collections import deque


def bfs(node_dict, visited, v):
    queue = deque([v])
    visited_nodes = []
    while queue:
        curr_node = queue.popleft()
        if visited[curr_node] is False:
            visited[curr_node] = True
            visited_nodes.append(curr_node)
            if curr_node in node_dict:
                for next_node in node_dict[curr_node]:
                    if visited[next_node] is False:
                        queue.append(next_node)
    return visited_nodes


def dfs(node_dict, visited, v):
    visited_nodes = []
    if visited[v] is False:
        visited[v] = True
        visited_nodes.append(v)
        if v in node_dict:
            for vertex in node_dict[v]:
                visited_nodes += dfs(node_dict, visited, vertex)
    return visited_nodes

def add_node(node_dict, a, b):
    if a in node_dict:
        node_dict[a].append(b)
    else:
        node_dict[a] = [b]


n, m, v = map(int, input().split())
node_dict = {}

for i in range(m):
    a, b = map(int,input().split())
    add_node(node_dict, a, b)
    add_node(node_dict, b, a)

for k, value in node_dict.items():
    value.sort()

for x in dfs(node_dict, [False for _ in range(n+1)], v):
    print(f"{x} ", end='')
print()
for y in bfs(node_dict, [False for _ in range(n+1)], v):
    print(f"{y} ", end='')

