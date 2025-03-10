def solution(t, p):
    answer = 0
    p_length = len(p)
    for i in range(len(t) - p_length + 1):
        sub_str = t[i:i+p_length]
        if int(sub_str) <= int(p):
            answer += 1
    
    return answer