from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for key, value in dic.items():
            if value == 1:
                return key
        return 0