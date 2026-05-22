#LC 3. Longest Substring Without Repeating Characters

#CODE:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        p1=0
        p2=1
        while p1<p2 and p2 <= len(s):
            if len(s[p1:p2+1]) == len(set(s[p1:p2+1])):
                l.append(len(s[p1:p2+1]))
                p2+=1
            else:
                p1 +=1
                p2 +=1
        if l:
            return max(l)
        return 0

            
        