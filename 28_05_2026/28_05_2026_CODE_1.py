#LC 137. Single Number II
#CODE:

import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        visited = []
        count = 0
        for i in nums:
            if i in visited:
                dic[i] +=1
            else:
                count +=1
                visited.append(i)
                dic.update({i:count})
                count = 0
        for key,value in dic.items():
            if value == 1:
                return key

        
                

        