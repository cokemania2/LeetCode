import itertools

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        normalized = [tuple(sorted(d)) for d in dominoes]
    
        counts = Counter(normalized)
    
        pairs = 0
        for count in counts.values():
            pairs += count * (count - 1) // 2  # nC2 계산
        return pairs
