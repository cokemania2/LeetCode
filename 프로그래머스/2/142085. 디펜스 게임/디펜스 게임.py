def solution(n, k, enemy):
    left, right = 0, len(enemy)
    answer = 0
    mid = 0
    while left <= right:
        mid = left + (right- left) // 2
        if sum(sorted(enemy[:mid])[:-k]) <= n:
            left = mid + 1
            answer = max(mid, answer)
        else:
            right = mid - 1
    return answer