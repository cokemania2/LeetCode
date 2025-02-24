def dfs(x, y, cnt, memo):
    if x == y:
        return cnt
    if x in relations:
        for v in relations[x]:
            if not memo[v]:
                memo[v] = True
                result = dfs(v, y, cnt + 1, memo)
                if result != -1:
                    return result
    return -1

n = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람
m = int(input()) # 부모 자식들 간의 관계의 개수

relations = dict()
memo =[False for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    if x in relations:
        relations[x].append(y)
    else:
        relations[x] = [y]
    if y in relations:
        relations[y].append(x)
    else:
        relations[y] = [x]  

memo[a] = True
print(dfs(a, b, 0, memo))
