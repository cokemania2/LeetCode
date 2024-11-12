def solution(sequence, k):
    answer = [0,0]
    
    n = len(sequence)
    min_interval = n
    end = start = 0 
    k_sum = 0
    
    for start in range(n):
        while k_sum < k and end < n:
            k_sum += sequence[end]
            end += 1
        if k_sum == k and end - 1 - start < min_interval:
            min_interval = end - 1 - start
            answer = [start, end - 1]
        k_sum -= sequence[start]
    return answer