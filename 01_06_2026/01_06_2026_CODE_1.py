#LC 8. String to Integer (atoi)
#CODE:

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        i=0
        s=s.lstrip()
        if not s:
            return 0
        if s[0]== "-":
            sign = -1
            i+=1
        if s[0] == "+":
            sign = +1
            i+=1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i+=1
        res = num * sign
        if res> (2**31 -1):
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        return res
        

            