from collections import deque

def is_clear(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                return False
    return True

def adjacent(y, x, max_y, max_x):
    answer = []
    if y - 1 >= 0:
        answer.append([y-1, x])
    if x - 1 >= 0:
        answer.append([y, x-1])
    if y + 1 < max_y:
        answer.append([y+1, x])
    if x + 1 < max_x:
        answer.append([y, x+1])
    return answer


def bfs(tomatos, arr, m, n):
    queue = deque(tomatos)
    last_count = 0
    while queue:
        curr_totmato = queue.popleft()
        y, x, count = curr_totmato
        if arr[y][x] == 0:
            arr[y][x] = 1
            last_count = count
            for next_y, next_x in adjacent(y, x, n, m):
                if arr[next_y][next_x] == 0:
                    queue.append([next_y, next_x, count + 1])
    return last_count

def find_start_tomatos(arr, n, m):
    start_tomatos = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 0
                start_tomatos.append([i, j, 0])
    return start_tomatos


m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

start_tomatos = find_start_tomatos(arr, n, m)

answer = bfs(start_tomatos, arr, m, n)
if is_clear(arr):
    print(answer)
else:
    print(-1)
