from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        딕셔너리로 변환 뒤 적은 갯수부터 차례로 키값을 제거
        """

        num_count = defaultdict(int)
        for v in arr:
            num_count[v] += 1
        
        sorted_num_count = sorted(num_count.items(), key=lambda x: x[1])
        for i, v in enumerate(sorted_num_count):
            k -= v[1]
            if k < 0:
                return len(sorted_num_count) - i
        return 0