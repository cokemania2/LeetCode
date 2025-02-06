from itertools import permutations
from collections import Counter

def is_prime(n):
    # 1과 0은 소수가 아님
    if n <= 1:
        return False
    
    # 2는 소수
    if n == 2:
        return True
    
    # 2로 나누어지면 소수가 아님
    if n % 2 == 0:
        return False
    
    # 3부터 n의 제곱근까지 홀수로 나누어 검사
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        num_list = permutations(list(numbers), i + 1)
        for num in num_list:
            answer.add(int(''.join(num)))
    return len([x for x in list(answer) if is_prime(x)])
