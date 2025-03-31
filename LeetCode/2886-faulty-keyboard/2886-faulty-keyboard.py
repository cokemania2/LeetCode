class Solution:
    def finalString(self, s: str) -> str:
        answer = []
        for v in s:
            if v == "i":
                answer.reverse()
            else:
                answer.append(v)
        return ''.join(answer)
