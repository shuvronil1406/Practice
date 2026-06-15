#Lc 88. Merge Sorted Array
#CODE

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []
        p1 = 0
        p2 = 0
        m = len(nums1) - len(nums2)
        while p1 < m and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1
        while p1 < m:
            res.append(nums1[p1])
            p1+=1
        while p2 < len(nums2):
            res.append(nums2[p2])
            p2+=1
        for i in range(len(res)):
            nums1[i] = res[i]
