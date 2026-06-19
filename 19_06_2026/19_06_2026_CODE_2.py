#LC 438. Find All Anagrams in a String
#CODE:

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        n= len(p)
        p1 = 0
        p2 = p1 + (n-1)
        ans=[]
        while p2<len(s):
            if sorted(s[p1:p2+1]) == p:
                ans.append(p1)
            p2+=1
            p1+=1
        return ans
        