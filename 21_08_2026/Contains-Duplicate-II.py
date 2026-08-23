#LC 219
#Solution

from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                if abs(mp[nums[i]] - i) <= k:
                    return True
                else:
                    mp[nums[i]] = i
        return False
        
        

            