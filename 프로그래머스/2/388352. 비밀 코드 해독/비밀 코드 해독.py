# 비밀 코드로 가능한 정수 조합 갯수
# 다 넣어보면 되겠네

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    combi = list(combinations(q, 5))[0]
    for c in combi:
        for i, _q in enumerate(q):
            count = 0
            for v in _q:
                print(v, c)
                if v in c:
                    count += 1
            print(count, ans[i])
            if count != ans[i]:
                break
        else:
            answer += 1
    return answer