#LC 242:
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(list)
        t_map = defaultdict(list)
        for i in s:
            count = 1
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i]+=1
        for j in t:
            count = 1
            if j not in t_map:
                t_map[j] = 1
            else:
                t_map[j]+=1
        return (s_map == t_map)
