class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b_s = bin(start)[2:]
        b_g = bin(goal)[2:]
        l_b_s = len(b_s)
        l_b_g = len(b_g)

        big_n, small_n = (b_s, b_g) if l_b_s >= l_b_g else (b_g, b_s)
        big_n = big_n[::-1]
        small_n = small_n[::-1]

        count = 0
        for i in range(len(big_n)):
            if len(small_n) <= i:
                if big_n[i] == '1':
                    count += 1
            elif small_n[i] != big_n[i]:
                count += 1
        return count