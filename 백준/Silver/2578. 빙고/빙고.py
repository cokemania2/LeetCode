def check_up_diag(board):
    for i in range(5):
        if board[i][4-i] != 0:
            break
    else:
        return 1
    return 0

def check_down_diag(board):
    for i in range(5):
        if board[i][i] != 0:
            break
    else:
        return 1
    return 0


def check_col(board, x):
    for y in range(5):
        if board[y][x] != 0:
            break
    else:
        return 1
    return 0

def check_row(board, y):
    for x in range(5):
        if board[y][x] != 0:
            break
    else:
        return 1
    return 0

def find_number(board, number):
    for y in range(5):
        for x in range(5):
            if board[y][x] == number:
                return y, x

def check_bingo(board, y, x):
    row_bingo = check_row(board, y)
    col_bingo = check_col(board, x)
    down_diagonal = check_down_diag(board) if (y==x) else 0
    up_diagonal = check_up_diag(board) if (y+x==4) else 0

    return row_bingo + col_bingo + down_diagonal + up_diagonal

answer = 0
bingo_board = []
call_numbers = []
for i in range(5):
    bingo_board.append(list(map(int, input().split())))

for i in range(5):
    call_numbers += list(map(int, input().split()))

for i in range(25):
    y, x = find_number(bingo_board, call_numbers[i])
    bingo_board[y][x] = 0
    answer += check_bingo(bingo_board, y, x)
    if answer >= 3:
        print(i+1)
        break

    