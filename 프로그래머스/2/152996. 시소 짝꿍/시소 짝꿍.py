from collections import Counter
import math

def is_couple(a, b):
    for i in [2, 3, 4]:
        for j in [2, 3, 4]:
            if a * i == b * j:
                return True
    return False

def solution(weights):
    counter = Counter(weights)
    set_weights = list(set(weights))
    
    answer = 0
    for i in range(len(set_weights)):
        for j in range(i+1, len(set_weights)):
            if is_couple(set_weights[i], set_weights[j]):
                answer += counter[set_weights[i]] * counter[set_weights[j]]

    # 같은 숫자끼리의 짝궁 계산
    for weight in counter:
        if counter[weight] > 1:
            answer += counter[weight] * (counter[weight] - 1) // 2
                
    return answer