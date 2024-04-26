def solution(n, m, section):
    answer = 0
    section_set = set(section)
    i = 0
    
    while i < n:
        if (i + 1) in section_set:
            answer += 1
            i += m  # 한번에 m만큼 이동
        else:
            i += 1  # 해당 섹션이 아니면 1만큼 이동
    
    return answer
