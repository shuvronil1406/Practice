class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
#LC 76. Minimum Window Substring
#CODE:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        
        required = len(need)
        formed = 0
        
        l = 0
        ans = [float("inf"), 0, 0]

        for r in range(len(s)):
            char = s[r]

            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while l <= r and formed == required:

                if (r - l + 1) < ans[0]:
                    ans = [r - l + 1, l, r]

                left_char = s[l]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        if ans[0] == float("inf"):
            return ""

        return s[ans[1]:ans[2] + 1]