#LC 46. Permutations

#CODE: 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        freq = [0]*len(nums)
        self.tree(ans,ds,freq,nums)
        return ans

    def tree(self,ans,ds,freq,nums):
        if len(ds) == len(nums):
            ans.append(ds[:])
        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = 1
                ds.append(nums[i])
                self.tree(ans,ds,freq,nums)
                ds.pop()
                freq[i] = 0