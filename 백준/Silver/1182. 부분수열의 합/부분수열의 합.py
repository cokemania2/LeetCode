from itertools import combinations

n, s = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

answer = 0 
for i in range(1, n+1):
    c_list = list(combinations(n_list, i))
    for c in c_list:
        if sum(c) == s:
            answer += 1
print(answer)