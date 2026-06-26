#LC 977. Squares of a Sorted Array
#CODE:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L=[i**2 for i in nums]
        L2 = sorted(L)
        return L2