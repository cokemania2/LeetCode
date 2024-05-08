def hanoi(start, end, mid, n, answer):
    if n == 1:
        answer.append([start, end])
    else:
        answer = hanoi(start, mid, end, n - 1, answer)
        answer = hanoi(start, end, mid, 1, answer)
        answer = hanoi(mid, end, start, n - 1, answer)
    return answer

def solution(n):
    return hanoi(1, 3, 2, n, [])