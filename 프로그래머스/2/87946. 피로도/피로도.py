from itertools import permutations

def solution(k, dungeons):
    max_case = 0
    
    cases = list(permutations([i for i in range(len(dungeons))]))
    for case in cases:
        stemina = k
        count = 0
        for v in case:
            if stemina >= dungeons[v][0]:
                stemina -= dungeons[v][1]
                count += 1 
            else:
                break
        max_case = max(max_case, count)
    
    return max_case