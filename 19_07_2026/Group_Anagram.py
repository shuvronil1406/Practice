#LC 49:
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        h_map = defaultdict(list) 
        for i in strs:
            sorted_s = tuple(sorted(i))
            h_map[sorted_s].append(i)
        for j in h_map.values():
            res.append(j)
        return res