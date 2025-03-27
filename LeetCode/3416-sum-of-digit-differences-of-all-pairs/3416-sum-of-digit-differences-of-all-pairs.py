class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        """
        각 숫자별로 자릿수에 몇개씩 존재하는지 count
        전체 갯수에서 빼기
        """

        arr = [[0 for _ in range(10)] for _ in range(len(str(nums[0])))]
        
        
        for num in nums:
            for i, v in enumerate(str(num)):
                arr[i][int(v)] += 1
        
        answer = 0
        n = len(nums)
        for v in arr:
            for i in range(10):
                if v[i] > 0:
                    answer += v[i] * (n - v[i])

        return answer // 2