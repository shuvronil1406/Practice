#LC 34. Find First and Last Position of Element in Sorted Array
#CODE: 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high= len(nums)-1
        L=[]

        while low  <= high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                L.append(mid)
                high = mid - 1 #searching the left for any occurence
            elif target<nums[mid]:
                high = mid-1
            elif target>nums[mid]:
                low=mid+1
        low=0
        high= len(nums)-1

        while low  <= high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                L.append(mid)
                low = mid + 1 #searching the right for any occurence
            elif target<nums[mid]:
                high = mid-1
            elif target>nums[mid]:
                low=mid+1
        if L:
            return ([min(L), max(L)])
        return -1,-1