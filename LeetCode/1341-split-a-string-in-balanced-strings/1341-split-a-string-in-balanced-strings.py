class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_stack = 0
        l_stack = 0

        answer = 0
        for v in s:
            if v == 'R':
                r_stack += 1
            else:
                l_stack += 1
            if r_stack > 0 and r_stack == l_stack:
                r_stack = 0
                l_stack = 0
                answer += 1
        return answer
