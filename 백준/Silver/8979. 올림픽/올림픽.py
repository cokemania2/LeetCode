N, K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank = 0
before = []
for i in range(len(arr)):
    if before != arr[i][1:]:
        rank += 1
        before = arr[i][1:]
    if arr[i][0] == K:
        print(rank)
        break
