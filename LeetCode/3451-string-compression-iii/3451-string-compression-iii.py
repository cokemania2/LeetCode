class Solution:
    def compressedString(self, word: str) -> str:
        answer = ""
        prefix = word[0]
        count = 0
        for w in word:
            if w == prefix:
                count += 1
                if count == 9:
                    answer += f'{count}{prefix}'
                    count = 0               
            else:
                if count > 0:
                    answer += f'{count}{prefix}'
                prefix = w
                count = 1

        return answer + (f'{count}{prefix}' if count > 0 else "")
