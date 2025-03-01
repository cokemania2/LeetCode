def binary_search(v, b):
    # v가 b를 먹을 수 있는 갯수
    left = 0
    right = len(b) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if v > b[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    count = 0
    for i in range(len(a)):
        count += binary_search(a[i], b)

    print(count)
