def solution(sizes):
    answer = 0
    x = sorted(sizes, key = lambda x : x[0])[-1][0]
    y = sorted(sizes, key = lambda x : x[1])[-1][1]
    
    max_x = max(x, y)
    max_y = 0
    for size in sizes:
        min_y = size[0] if size[0] < size[1] else size[1]
        max_y = max(min_y, max_y)
    
    return max_x * max_y