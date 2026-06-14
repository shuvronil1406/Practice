#LC 3. Longest Substring Without Repeating Characters
#CODE:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        mp = {}
        max_l = 0
        while r < len(s):
            if s[r] in mp:
                if mp[s[r]] >= l:
                    # length = l - r + 1
                    max_l = max(max_l,r-l)
                    l = mp[s[r]]+1
            mp[s[r]] = r
            r+=1
        # length = l - r + 1
        max_l = max(max_l,r-l)
        return max_l
