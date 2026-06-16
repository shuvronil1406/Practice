#LC 42. Trapping Rain Water
#CODE

class Solution:
    def trap(self, height: List[int]) -> int:

    #min(maxLeft,maxRight) - height[i]
        cap = 0
        prefixMax = [0] * len(height)
        suffixMax = [0] * len(height)
        prefixMax[0]= height[0]
        for i in range(1,len(height)):
            prefixMax[i] = max(prefixMax[i-1], height[i])
        suffixMax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suffixMax[i] = max(suffixMax[i+1],height[i])
        for i in range(len(height)):
            maxLeft = prefixMax[i]
            maxRight = suffixMax[i]
            cap+= min(maxLeft,maxRight) - height[i]
        return cap

