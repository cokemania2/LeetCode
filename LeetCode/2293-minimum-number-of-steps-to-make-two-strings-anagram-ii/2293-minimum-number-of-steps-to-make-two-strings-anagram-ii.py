"""
1. 각각 [a-z]까지 알파벳의 갯수를 샌다 (딕셔너리)
2. s의 딕셔너리를 돌며 t에는 있는지 확인
    - 갯수가 적거나 없으면 count 증가
2. t의 딕셔너리를 돌며 s에는 있는지 확인
    - 갯수가 적거나 없으면 count 증가
return count
"""

from collections import Counter

def count_characters(s):
    return dict(Counter(s))

def compare_count(a, b):
    count = 0
    for key, value in a.items():
        if key in b:
            if value > b[key]:
                count +=  (value - b[key])
        else:
            count += value 
    return count

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        step = 0
        s_dict = count_characters(s)
        t_dict = count_characters(t)
        return compare_count(s_dict, t_dict) + compare_count(t_dict, s_dict)