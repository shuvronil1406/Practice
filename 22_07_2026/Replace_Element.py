#LC 1299
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res=[1] * n
        max_el = -1
        res[-1] = -1
        for i in range(n-1,0,-1):
            if arr[i] > max_el:
                res[i-1] = arr[i]
                max_el = arr[i]
            else:
                res[i-1] = max_el
        return res