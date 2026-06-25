#LC 26. Remove Duplicates from Sorted Array
#CODE:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1= 0
        p2 = 1
        while  p1<=p2 and p2< len(nums):
            if nums[p2] != nums[p1]:
                nums[p1+1] = nums[p2]
                p2+=1
                p1+=1
            else:
                p2+=1
        return p1+1
            

