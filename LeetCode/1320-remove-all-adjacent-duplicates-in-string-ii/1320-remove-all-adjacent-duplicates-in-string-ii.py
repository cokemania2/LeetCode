class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for v in s:
            if len(stack) > 0 and stack[-1][0] == v:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([v, 1])
        return "".join(char * count for char, count in stack)