#LC 242. Valid Anagram
#CODE:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t))