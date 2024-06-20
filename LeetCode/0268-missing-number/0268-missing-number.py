class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        nums = sorted(nums)
        
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == mid:
                start = mid + 1
            else:
                end = mid
                
        return start