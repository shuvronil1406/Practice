#LC 14. Longest Common Prefix
#CODE :

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = ""
        if not strs[0]:
            return p
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range (1, len(strs)):
                if i >= len(strs[j]):
                    return p
                elif strs[j][i] ==  char:
                    flag = 1
                else:
                    return p
            p+= char
        return p