from itertools import product

def can_ban(u_id, b_id):
    for i in range(len(b_id)):
        if b_id[i] != "*" and u_id[i] != b_id[i]:
            return False
    return True

def get_unique_combinations(data):
    unique_results = set()
    
    for combination in product(*data):
        if len(set(combination)) == len(combination):  # 중복 체크
            unique_results.add(tuple(sorted(combination)))  # 정렬 후 추가
    
    return list(unique_results)

def solution(user_id, banned_id):
    jejes = []
    for b in banned_id:
        b_list = [] # 밴 가능한 목록
        b_length = len(b)
        for u in user_id:
            if b_length == len(u) and can_ban(u, b):
                b_list.append(u)
        jejes.append(b_list)
    
    return len(get_unique_combinations(jejes))
