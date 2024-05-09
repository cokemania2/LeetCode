import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n in [2 ** i for i in range(-31, 32, 1)] else False