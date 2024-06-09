def solution(storey):
    answer = 0
    digit = 0
    while storey != 0:
        print(storey, end=' ')
        # 첫째 자리부터 순서대로
        x = str(storey)[::-1]
        target_n = int(x[digit])
        next_target_n = int(x[digit + 1]) if len(x) > digit + 2 else None
        # 6 이상이면 올리는게 이득
        if target_n >= 6 or (target_n == 5 and next_target_n and next_target_n >= 5):
            stone = (10 - target_n)
            storey += stone * (10**digit)
        else:
            stone = target_n
            storey -= stone * (10**digit)
        print(storey, stone)
        digit += 1
        answer += stone
    return answer