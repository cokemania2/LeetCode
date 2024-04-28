class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        nums1의 index인 i는 작을수록 좋고 nums2의 indexd인 j는 클수록 좋다.
        nums1[0]과 nums2[0]먼저 비교하여 nums1[0]이 nums2[0]보다 클 경우
        i += 1 을 하여, nums1의 최솟값을 충족시킨다.
        반복하여 최솟값을 충족시켰다면, nums2의 index값인 j를 올려서 거리를 최대화 한다.
        """
        
        answer = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                answer = max(j - i, answer)
                j += 1
        return answer


                
            