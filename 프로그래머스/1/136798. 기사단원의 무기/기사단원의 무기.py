"""
기사 단원은 15의 "약수만큼의 공격력을 가진 무기" 구매
제약사항이 있고, 제한을 초과하면 지정 공격력을 가진 무기를 구매해야함.
"""

def get_divisors(number):
    divisors = [0 for _ in range(number + 1)]
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if i * j > number:
                break
            divisors[i * j] += 1
    return divisors


def solution(number, limit, power):
    divisors = get_divisors(number)
    answer = 0
    for i in range(1, number + 1):
        v = divisors[i]
        if v > limit:
            answer += power
        else:
            answer += v

    return answer