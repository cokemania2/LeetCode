from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        x = defaultdict(int)
        
        total_pairs = len(nums) * (len(nums) - 1) // 2 # 콤비네이션
        good_pairs = 0
        for i, num in enumerate(nums):
            key = i - num
            good_pairs += x[key]
            x[key] += 1

        return total_pairs - good_pairs
