def solution(dirs):
    SIZE = 11

    def move(direction, cord):
        new_cord = cord[:]
        if direction == "U" and new_cord[0] > 0:
            new_cord[0] -= 1
        elif direction == "D" and new_cord[0] < SIZE - 1:
            new_cord[0] += 1
        elif direction == "R" and new_cord[1] < SIZE - 1:
            new_cord[1] += 1
        elif direction == "L" and new_cord[1] > 0:
            new_cord[1] -= 1
        return new_cord

    # 이동 경로 추적
    answer = 0
    current = [5, 5]  # 시작 좌표 (중앙)
    passed_routes = set()  # 지나간 경로 저장

    for direction in dirs:
        next_position = move(direction, current)
        if current == next_position:
            continue
        # 이전 좌표와 현재 좌표를 경로로 저장
        new_route = frozenset((tuple(current), tuple(next_position)))
        if new_route not in passed_routes:
            passed_routes.add(new_route)
            answer += 1
        current = next_position  # 현재 위치 갱신

    return answer