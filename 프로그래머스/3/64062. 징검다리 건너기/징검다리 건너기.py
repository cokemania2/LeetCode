def solution(stones, k):
    answer = 0
    
    min_stone = min(stones)
    max_stone = max(stones)
    while min_stone <= max_stone:   
        mid_stone = (min_stone + max_stone) // 2
        count = 0
        for stone in stones:
            if stone <= mid_stone:
                count += 1
                if count >= k:
                    max_stone = mid_stone - 1
                    break
            else:
                count = 0
        else:
             min_stone = mid_stone + 1
        
    return min_stone