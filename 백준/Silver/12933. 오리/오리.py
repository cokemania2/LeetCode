def solution():
    s = input().strip()
    quack = "quack"
    ducks = []
    answer = 0

    if s[0] != "q":  # 첫 문자가 'q'가 아니라면 불가능한 경우
        return -1

    for v in s:
        idx = quack.find(v)  # 현재 문자가 'quack'에서 몇 번째인지 찾기
        if idx == 0:
            ducks.append([v])  # 새로운 오리 시작
        else:
            found = False
            to_remove = []
            for duck in ducks:
                if len(duck) == idx:  # 올바른 순서로 울고 있는 오리 찾기
                    duck.append(v)
                    if v == "k":
                        to_remove.append(duck)  # 나중에 제거할 리스트에 추가
                    found = True
                    break
            if not found:
                return -1
            for duck in to_remove:
                ducks.remove(duck)  # 'k'까지 다 운 오리 제거

        answer = max(answer, len(ducks))

    return answer if not ducks else -1

print(solution())