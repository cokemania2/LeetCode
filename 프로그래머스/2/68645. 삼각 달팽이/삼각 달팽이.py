def solution(n):
    answer = []
    arr_list = [[0 for j in range(n)] for i in range(n)]
    
    y = -1
    x = 0
    v = 1
    yd = 1
    xd = 0
    for i in range(n, 0, -1):
        for j in range(i):
            y += yd
            x += xd
            arr_list[y][x] = v
            v += 1
        if (n - i) % 3 == 0:
            yd = 0
            xd = 1
        elif (n - i) % 3 == 1:
            yd = -1
            xd = -1
        elif (n - i) % 3 == 2:
            yd = 1
            xd = 0

    for i in range(n):
        answer += arr_list[i][:i+1]
    return answer