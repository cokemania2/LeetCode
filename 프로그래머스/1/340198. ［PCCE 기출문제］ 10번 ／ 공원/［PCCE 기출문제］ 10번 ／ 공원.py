def solution(mats, park):
    _map = [[0 for _ in range(len(park[i]))] for i in range(len(park))]
    _max = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                if i == 0 or j == 0:
                    _map[i][j] = 1
                else:
                    top = _map[i-1][j]
                    left = _map[i][j-1]
                    top_left = _map[i-1][j-1]
                    _map[i][j] = top + 1 if top == left == top_left != 0 else min(top, left, top_left) + 1
                    _max = max(_map[i][j], _max)
    
    _answer = -1
    mats.sort()
    for mat in mats:
        if mat <= _max:
            _answer = mat
    return _answer