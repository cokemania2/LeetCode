# 절단기 높이의 **최댓값**을 찾아야한다.

def binary_search(start, end, n_list, M):
    mid = 0
    while start <= end:
        # mid는 자르는 나무 인덱스
        mid = start + (end - start) // 2
        cutted = 0
        for n in n_list:
            if n > mid:
                cutted += n - mid
        if cutted < M:
            end = mid - 1
        else:
            start = mid + 1
    return end

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.append(0)
n_list.sort()

start = 0
end = max(n_list)
x = binary_search(start, end, n_list, M)
print(x)
