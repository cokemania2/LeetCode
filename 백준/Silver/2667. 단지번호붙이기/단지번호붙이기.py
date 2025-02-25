from collections import deque

N = int(input())

dange = []
for i in range(N):
    dange.append(list(map(int, list(input()))))

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(y, x):
    queue = deque([[y, x]])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    
    dange_count = 1
    visited[y][x] = True
    while len(queue) > 0:
        y, x = queue.popleft()
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and not visited[y + dy[i]][x + dx[i]] and dange[y + dy[i]][x + dx[i]] == 1:
                visited[y+dy[i]][x+dx[i]] = True
                queue.append([y + dy[i], x + dx[i]])
                dange_count += 1
    return dange_count

answer = []
for i in range(N):
    for j in range(N):
        if dange[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])
