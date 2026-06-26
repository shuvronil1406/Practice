#LC 128. Longest Consecutive Sequence
#CODE:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        largest=0
        count=0
        x=0
        for i in s:
            if i-1 not in s:
                x=i
                count=1
            while x+1 in s:
                count+=1
                x=x+1
            if count>largest:
                largest=count
        return largest

        