from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    orders_list = list(permutations([i for i in range(len(dungeons))]))
    max_count = 0
    for orders in orders_list:
        remain_k = k
        for i, order in enumerate(orders):
            minimum, consume = dungeons[order]
            if remain_k >= minimum and remain_k >= consume:
                remain_k -= consume
            else:
                max_count = max(max_count, i)
                break
        else:
            return len(dungeons)
        
    return max_count