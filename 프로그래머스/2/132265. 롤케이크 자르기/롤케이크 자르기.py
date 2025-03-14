# 동일한 가짓수로 나누면 == 공평하다
# 왼쪽에서부터, 오른쪽에서 부터 오면서 set의 count를 누적하고
# 옆의 count와 같을때... 가 정답이지 않을까

def get_topping_set_list(topping):
    topping_set = set()
    set_list = []
    
    for v in topping:
        topping_set.add(v)
        set_list.append(len(topping_set))

    return set_list

def solution(topping):
    answer = 0
    
    reverse_cake = reversed(topping)
    
    topping_set_list = get_topping_set_list(topping)
    reversed_topping_set_list = list(reversed(get_topping_set_list(reverse_cake)))
    
    for i in range(1, len(topping_set_list)):
        if topping_set_list[i - 1] == reversed_topping_set_list[i]:
            answer += 1
    
    return answer