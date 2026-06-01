#LC 2042. Check if Numbers Are Ascending in a Sentence
#CODE:

import re
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        L=[]
        L=[int(i) for i in re.findall(r'\d+',s)]
        for i in range(len(L)-1):
            if L[i] >= L[i+1]:
                return False
        return True
