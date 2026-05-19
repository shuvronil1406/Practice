#LC 136. Single Number

#CODE: 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        visited = []
        for i in nums:
            if i not in visited:
                visited.append(i)
                count += 1
                dic.update({i:count})
                count = 0
            else:
                dic[i]+=1
        for i in dic.keys():
            if dic[i] == 1:
                return i