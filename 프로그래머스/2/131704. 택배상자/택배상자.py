def solution(order):
    stack = []  # 보조 컨테이너 벨트 역할
    answer = 0  # 트럭에 실은 상자 수
    belt_position = 0  # 컨테이너 벨트의 현재 위치
    n = len(order)  # 상자의 총 개수

    # 벨트에서 상자를 꺼내면서 원하는 상자를 찾는 루프
    for box in range(1, n + 1):
        if box == order[belt_position]:  # 컨테이너 벨트에서 바로 원하는 상자가 나온다면
            answer += 1
            belt_position += 1  # 다음 필요한 상자로 이동
            # 스택에서 필요한 상자가 나오면 계속 트럭에 싣는다
            while stack and stack[-1] == order[belt_position]:
                stack.pop()
                answer += 1
                belt_position += 1
        else:  # 원하는 상자가 아니라면 스택에 보관
            stack.append(box)

    return answer
