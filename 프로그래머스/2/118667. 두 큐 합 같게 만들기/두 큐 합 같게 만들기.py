def solution(queue1, queue2):
    queue = queue1 + queue2
    target = sum(queue) // 2
    
    if sum(queue) % 2 != 0:
        return -1
    
    n = len(queue1)
    start, end = 0, n
    current_sum = sum(queue1)
    move_count = 0
    
    while start < 2*n and end < 2*n:
        if current_sum == target:
            return move_count
        elif current_sum < target and end < 2*n:
            current_sum += queue[end]
            end += 1
            move_count += 1
        else:
            current_sum -= queue[start]
            start += 1
            move_count += 1
    
    return -1