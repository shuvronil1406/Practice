#LC 38. Count and Say

#CODE:

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            s = "1"
            return s
        say = self.countAndSay(n-1)
        #processing:
        res = ""
        i=0
        while i < len(say):
            char = say[i]
            count = 1
            while i<len(say)-1 and say[i]==say[i+1]:
                count +=1
                i+=1
            res += str(count) + char
            i+=1
        return res


