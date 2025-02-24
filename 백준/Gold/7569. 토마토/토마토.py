# BFS
from collections import deque

# 익은 토마토 찾기
def find_ripe_tomatos():
    ripe_tomatos = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    ripe_tomatos.append((i, j, k, 0))
    return ripe_tomatos

def is_there_any_unriped_tomato():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return True
    return False

M, N, H = map(int, input().split()) # 상자의 크기
box = []
for i in range(H):
    box.append([list(map(int, input().split())) for j in range(N)])

ripe_tomatos = find_ripe_tomatos()
queue = deque(ripe_tomatos)
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

max_day = 0
while queue:
    z, x, y, day = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = box[z][x][y] + 1
            queue.append((nz, nx, ny, day + 1))
            if day + 1 > max_day:
                max_day = day + 1

print(max_day if not is_there_any_unriped_tomato() else -1)