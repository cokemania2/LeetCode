# n^2 * logN 예상
# 모든 substring을 찾아서 1의 갯수 확인하기

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        answer = s + "k"
        for i in range(len(s)):
            for j in range(i+1, len(s)+ 1):
                if s[i:j].count("1") == k and len(s[i:j]) <= len(answer):
                    if len(s[i:j]) == len(answer) and s[i:j] > answer:
                        continue
                    answer = s[i:j]
        return answer if answer != s + "k" else ""
