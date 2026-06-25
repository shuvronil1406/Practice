#LC 349. Intersection of Two Arrays
#CODE:

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L=[]
        n1= len(nums1)
        n2= len(nums2)
        if n1 < n2:
            for i in range(n1):
                if nums1[i] in nums2:
                    L.append(nums1[i])
        else:
            for i in range(n2):
                if nums2[i] in nums1:
                    L.append(nums2[i])
        return list(set(L))
        