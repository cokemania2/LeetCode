from functools import reduce
from collections import Counter

def solution(clothes):
    total_combinations = 1

    clothes_dict = Counter([category for _, category in clothes])
    total_combinations = reduce(lambda x, y: x * (y + 1), clothes_dict.values(), 1)
    
    return total_combinations - 1
        