#LC 20290


#Solution:

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr2= [-1] * n
        if n < 2 * k + 1:
            return arr2
        i = k
        p1 = 0
        p2 = 2 *k 
        s = sum(nums[p1: p2+1])
        while i < n-k:
            arr2[i] = s // (2*k + 1)
            if i+1 < n-k:
                s = s - nums[p1] + nums[p2+1]
                p1 += 1
                p2 += 1
            i+=1
        # if i==k:
        #     return nums
        return arr2