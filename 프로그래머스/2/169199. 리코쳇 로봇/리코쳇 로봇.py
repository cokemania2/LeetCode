from collections import deque


def slide(board, y, x, mul_y, mul_x):
    max_y = len(board)
    max_x = len(board[0])
    while True:
        y += mul_y
        x += mul_x
        if x >= max_x or y >= max_y or y < 0 or x < 0 or board[y][x] == "D":
            return y - mul_y if mul_y != 0 else x - mul_x


def bfs(queue, board):
    while True:
        if len(queue) == 0:
            return -1
        point = queue.popleft()
        y, x, count = point[0], point[1], point[2]
        if board[y][x] == "G":
            return count
        board[y][x] = "X"

        up_y = slide(board, y, x, 1, 0) # up
        if y != up_y and board[up_y][x] != "X":
            queue.append([up_y, x, count + 1])
        down_y = slide(board, y, x, -1, 0) # down
        if y != down_y and board[down_y][x] != "X":
            queue.append([down_y, x, count + 1])
        right_x = slide(board, y, x, 0, 1) # right
        if x != right_x and board[y][right_x] != "X":
            queue.append([y, right_x, count + 1])
        left_x = slide(board, y, x, 0, -1) # left
        if x != left_x and board[y][left_x] != "X":
            queue.append([y, left_x, count + 1])

def solution(board):
    for y in range(len(board)):
        board[y] = list(board[y])
        for x in range(len(board[y])):
            if board[y][x] == "R":
                start_y, start_x = y, x
    queue = deque([[start_y, start_x, 0]])
    return bfs(queue, board)