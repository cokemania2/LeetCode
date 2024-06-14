class Solution:
    def change(self, s: str, index: int) -> str:
        s_list = list(s)
    
        tmp = s_list[index + 2]
        s_list[index + 2] = s_list[index]
        s_list[index] = tmp
        return ''.join(s_list)

    def can_change_list(self, s: str) -> list[str]:
        return [s, self.change(s, 0), self.change(s, 1), self.change(self.change(s, 0), 1)]

    def canBeEqual(self, s1: str, s2: str) -> bool:
        return True if s1 in self.can_change_list(s2) or s2 in self.can_change_list(s1) else False