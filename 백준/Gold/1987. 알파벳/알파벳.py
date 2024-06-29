import sys
input = sys.stdin.readline

def dfs(y, x, count):
    global answer
    answer = max(answer, count)
    
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and not visited[ord(board[ny][nx]) - 65]:
            visited[ord(board[ny][nx]) - 65] = True
            dfs(ny, nx, count + 1)
            visited[ord(board[ny][nx]) - 65] = False

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

visited = [False] * 26
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 1
visited[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)

print(answer)