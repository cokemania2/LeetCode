def solution(name, yearning, photo):
    answer = []
    name_yearning_dict = {}
    for n, y in zip(name, yearning):
        name_yearning_dict[n] = y
    for p in photo:
        score = 0
        for photo_name in p:
            if photo_name in name_yearning_dict:
                score += name_yearning_dict[photo_name]
        answer.append(score)
    return answer
