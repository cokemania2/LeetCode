def solution(arr):
    answer = []
    
    for v in arr:
        if len(answer) != 0 and answer[-1] == v:
            continue
        answer.append(v)
    
    return answer