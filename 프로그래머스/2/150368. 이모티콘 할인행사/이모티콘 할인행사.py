import itertools

def get_user_cost(case, user, emoticons):
    min_discount_rate, max_cost = user
    
    cost = 0
    is_joined = False
    for discount_rate, emoticon_cost in zip(case, emoticons):
        if discount_rate >= min_discount_rate:
            cost += emoticon_cost * (1 - discount_rate / 100)
    if cost >= max_cost:
        return (True, 0)
    return (False, cost)

def get_all_discount_cases(emoticons):
    DISCOUNT_RATES = [10, 20, 30, 40]
    
    all_cases = list(itertools.product(DISCOUNT_RATES, repeat=len(emoticons)))
    return all_cases

def solution(users, emoticons):
    answer = [0, 0]
    
    # 할인율은 4개, 이모티콘은 최대 7개. 유저는 100명. 경우의수가 얼마 없다. 
    # 모든 경우를 구하는게 좋을듯
    cases = get_all_discount_cases(emoticons)
    for case in cases:
        joined_user = 0
        all_cost = 0
        for user in users:
            is_join, cost = get_user_cost(case, user, emoticons)
            joined_user += 1 if is_join else 0
            all_cost += cost
        
        if joined_user > answer[0]:
            answer = [joined_user, all_cost]
        elif joined_user == answer[0]:
            answer[1] = max(answer[1], all_cost)
    
    return answer