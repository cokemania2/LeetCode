class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for i in range(1, n + 1):
            answer.append(bin(i)[2:].count('1'))
        
        return answer