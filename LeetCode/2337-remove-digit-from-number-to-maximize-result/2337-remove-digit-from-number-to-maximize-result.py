class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return str(max([int(number[:i] + number[i+1:]) for i, n in enumerate(number) if n == digit]))
