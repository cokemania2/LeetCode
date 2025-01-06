def solution(ingredient):
    answer = 0
    stack = []
    for v in ingredient:
        if v == 1:
            if len(stack) > 0 and len(stack[-1]) == 3 and  stack[-1][-1] == 3:
                answer += 1
                stack.pop()
            else:
                stack.append([v])
        elif v == 2:
            if len(stack) > 0 and stack[-1][-1] == 1:
                stack[-1].append(v)
            else:
                stack.append([v])
        elif v == 3:
            if len(stack) > 0 and stack[-1][-1] == 2:
                stack[-1].append(v)
            else:
                stack.append([v])
    return answer