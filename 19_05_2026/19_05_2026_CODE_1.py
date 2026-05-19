#LC 58. Length of Last Word

#CODE:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split()
        return len(s[-1])
        