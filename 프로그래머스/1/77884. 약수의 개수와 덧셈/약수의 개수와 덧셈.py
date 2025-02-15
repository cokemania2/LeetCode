def solution(left, right):
    dp = [0 for _ in range(1001)]
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i * j > 1000:
                break
            dp[i * j] += 1
    
    return sum([i if dp[i] % 2 == 0 else -i for i in range(left, right + 1)])