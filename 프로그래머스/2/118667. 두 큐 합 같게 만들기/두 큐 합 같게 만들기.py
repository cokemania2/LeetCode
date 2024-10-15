def solution(queue1, queue2):
    answer = -2
    
    queue = queue1 + queue2
    half_sum = sum(queue) / 2
    
    candidates = []
    for i in range(1, len(queue) + 1):
        for j in range(len(queue)):
            if sum(queue[j:j+i]) == half_sum:
                print(queue[j:j+i], queue[j+i:] + queue[:j])
                candidates.append(queue[j:j+i])
    
    
    
    return answer