import math

INF = math.inf

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [INF] * (k + 1)
dp[0] = 0  # 0원을 만드는 데 필요한 동전의 수는 0

for coin in coins:
    if coin <= k:  # coin이 k보다 작거나 같은 경우에만 처리
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != INF else -1)