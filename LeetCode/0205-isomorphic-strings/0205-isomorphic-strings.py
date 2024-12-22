class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        change_dict = dict()
        destiny_set = set()
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] in change_dict:
                s[i] = change_dict[s[i]]
            else:
                if t[i] not in destiny_set:
                    destiny_set.add(t[i])
                    change_dict[s[i]] = t[i]
                    s[i] = t[i]
                else:
                    return False
        return s == t
        