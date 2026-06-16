#LC 238. Product of Array Except Self
#CODE

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]* n
        left = [1] * n
        answer =[1] * n
        #building left :
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        #building right
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        for j in range(n):
            answer[j] = right[j] * left[j]
        
        return answer