#LC 128

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i-1 not in s:
                l = 0
                while (i+l) in s:
                    l+=1
                longest = max(l, longest)
        return longest