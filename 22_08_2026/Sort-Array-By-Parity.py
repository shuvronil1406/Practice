#LC 905:
#Solution

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # mp = [0] * 5000
        # for i in nums:
        #     mp[i]+=1
        # res=[]
        # for i in range(len(mp)):
        #     if mp[i] and i%2 == 0:
        #         res.append(i)
        #         mp[i]-=1
        # for i in range(len(mp)):
        #     if mp[i] and i%2 != 0:
        #         res.append(i)
        #         mp[i]-=1
        # return res
        even = [i for i in nums if i%2 == 0]
        odd = [i for i in nums if i%2 != 0]

        even.sort()
        odd.sort()
        return even+odd