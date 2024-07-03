"""
a: int # 운반 되어야 하는 금
b: int # 운반 되어야 하는 은
g: list[int] # 도시별 금 보유량
s: list[int] # 도시별 은 보유량
w: list[int] # 도시별 운반 가능량
t: list[int] # 도시별 운반 시간
"""


def solution(a, b, g, s, w, t):
    answer = -1
    cities_length = len(g)
    min_time = 0
    max_time = get_max_time(g, s, w, t, cities_length)
    
    while min_time < max_time:
        mid_time = min_time + (max_time - min_time) // 2
        carry_sum = 0
        max_silver = 0
        max_gold = 0
        
        for i in range(cities_length):
            transport_times = (mid_time // t[i]) # 편도 이동 가능 횟수
            can_carry = w[i] * (transport_times // 2 + transport_times % 2)
            carry_sum += min(can_carry, g[i] + s[i])
            max_silver += min(can_carry, s[i])
            max_gold += min(can_carry, g[i])
        if (carry_sum < a + b) or (max_silver < b) or (max_gold < a):
            min_time = mid_time + 1
        else:
            max_time = mid_time
    return max_time


def get_max_time(g, s, w, t, cities_length):
    max_time = 0
    for i in range(cities_length):
        max_time += ((g[i] + s[i]) // w[i] + 1) * (t[i] * 2)
    return max_time