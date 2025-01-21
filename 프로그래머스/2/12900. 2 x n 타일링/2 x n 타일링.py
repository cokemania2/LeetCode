def solution(n):
    answer = 0
    
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append((dp[i-1] + dp[i-2]) % 1_000_000_007) 
    return dp[n]