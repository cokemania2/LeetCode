from collections import deque

def bfs(maps, is_checked, i, j, heights, raws):
    queue = deque([[i, j]])
    answer = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while len(queue) > 0:
        y, x = queue.popleft()
        answer += int(maps[y][x])
        for i in range(4):
            if 0 <= dy[i] + y < heights and 0 <= dx[i] + x < raws:
                if maps[y + dy[i]][x + dx[i]] != 'X' and not is_checked[y + dy[i]][x + dx[i]]:
                    queue.append([y + dy[i], x + dx[i]])
                    is_checked[y + dy[i]][x + dx[i]] = True
    return answer

def solution(maps):
    answer = []
    
    heights = len(maps)
    raws = len(maps[0])
    
    is_checked = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(heights):
        for j in range(raws):
            if maps[i][j] != 'X' and not is_checked[i][j]:
                is_checked[i][j] = True
                answer.append(bfs(maps, is_checked, i, j, heights, raws))
    
    return sorted(answer) if len(answer) != 0 else [-1]