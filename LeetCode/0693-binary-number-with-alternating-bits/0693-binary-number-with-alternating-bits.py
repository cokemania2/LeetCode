class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a, b = -1, -1
        while n != 0:
            a = n % 2
            if a == b:
                return False
            b = a
            n //= 2
        return True
