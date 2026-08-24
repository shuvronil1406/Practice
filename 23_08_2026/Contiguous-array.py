#LC 525

#Solution:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        mp ={0:-1}
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -=1
            else:
                prefix +=1
            if prefix in mp:
                length = i - mp[prefix]
                ans = max(length, ans)
            else:
                mp[prefix] = i
        return ans