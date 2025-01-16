def is_over_or_block(park, now_loc, y, x):
    if now_loc[0] + y >= len(park) or now_loc[0] + y < 0 or now_loc[1] + x >= len(park[0]) or now_loc[1] + x < 0:
        return True
    if park[now_loc[0] + y][now_loc[1] + x] == "X":
        return True
    return False

def move_loc(park, now_loc, y, x, times):
    for i in range(1, times + 1):
        if is_over_or_block(park, now_loc, y * i, x * i):
            break
    else:
        now_loc[0] = now_loc[0] + y * times
        now_loc[1] = now_loc[1] + x * times

def move(park, direction, times, now_loc):
    if direction == "N":
        move_loc(park, now_loc, -1, 0, times)
    elif direction == "S":
        move_loc(park, now_loc, 1, 0, times)
    elif direction == "W":
        move_loc(park, now_loc, 0, -1, times)
    elif direction == "E":
        move_loc(park, now_loc, 0, 1, times)
    return now_loc

def find_start(park):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                return [i, j]

def solution(park, routes):
    now_loc = find_start(park)
    for route in routes:
        direction, times = route.split()
        move(park, direction, int(times), now_loc)
    return now_loc