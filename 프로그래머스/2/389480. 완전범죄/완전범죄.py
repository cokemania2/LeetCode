def func(info, step, n, max_n, m, max_m, memo):
    if step == len(info):
        if n < max_n and m < max_m:
            return n
        return float('inf')
    
    x = (step, n, m)
    if x in memo:
        return memo[x]
    
    if n >= max_n or m >= max_m:
        return float('inf')
    
    answer = min(
        func(info, step + 1, n + info[step][0], max_n, m, max_m, memo),
        func(info, step + 1, n, max_n, m + info[step][1], max_m, memo)
    )
    memo[x] = answer
    return answer

def solution(info, n, m):
    answer = func(info, 0, 0, n, 0, m, dict())
    return answer if answer != float('inf') else -1
