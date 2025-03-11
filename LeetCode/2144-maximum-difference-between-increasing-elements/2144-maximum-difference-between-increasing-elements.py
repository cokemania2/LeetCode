class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # 앞으로 전진하며 최솟값을 찾는다.
        # 그리고 diff값을 계산한다.

        _min, diff = nums[0], -1
        for i in range(1, len(nums)):
            if nums[i] - _min > 0:
                diff = max(diff, nums[i] - _min)
            if nums[i] < _min:
                _min = nums[i]
        
        return diff