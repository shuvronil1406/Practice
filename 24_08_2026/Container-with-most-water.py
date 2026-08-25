#LC 11. Container With Most Water
#Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        l= 0
        r = n -1
        max_weight = 0
        while l<r:
            w = r - l
            ht = min(height[l], height[r])
            curr = ht * w
            max_weight = max(max_weight,curr)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_weight