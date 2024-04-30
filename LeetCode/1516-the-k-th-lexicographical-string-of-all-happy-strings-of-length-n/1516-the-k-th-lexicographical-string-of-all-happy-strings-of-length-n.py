import itertools

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        string_list = list(itertools.product(letters, repeat=n))
        happy_strings = self._get_happy_strings(string_list)
        happy_strings.sort()
        
        return "".join(happy_strings[k - 1]) if k <= len(happy_strings) else ""
    
    def _get_happy_strings(self, string_list: list[str]) -> list[str]:
        happy_strings = []
        for s in string_list:
            for i in range(1, len(s)):
                if s[i-1] == s[i]:
                    break
            else:
                happy_strings.append(s)
        return happy_strings
                