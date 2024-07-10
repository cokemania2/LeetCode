N = int(input())
n_list = list(map(int, input().split()))
m = int(input())

n_list.sort()

left, right = 0, n_list[-1]
answer = 0

while left <= right:
    mid = (left + right) // 2
    budget = 0
    
    for i in range(N):
        if n_list[i] <= mid:
            budget += n_list[i]
        else:
            budget += (N - i) * mid
            break
    
    if budget <= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)