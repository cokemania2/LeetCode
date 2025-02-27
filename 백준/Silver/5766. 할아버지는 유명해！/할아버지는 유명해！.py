from collections import Counter

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    scores = []
    for i in range(N):
        scores += list(map(int, input().split()))
    score_count = Counter(scores)
    rank = sorted(score_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 두번쨰 랭킹부터 출력하기
    first = rank[0][1]
    second = rank[1][1]
    answer = []
    flag = False
    for i in range(1, len(rank)):
        if rank[i][1] == second:
            answer.append(rank[i][0])
        else:
            break
    print(*answer)
