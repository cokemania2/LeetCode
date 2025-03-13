def solution(elements):
    answer_set = set()
    circle_elements = elements + elements
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            answer_set.add(sum(circle_elements[j:j+i]))
    return len(answer_set)