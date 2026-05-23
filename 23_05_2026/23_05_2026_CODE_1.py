#LC 29. Divide Two Integers
#CODE:


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        sign = True
        if divisor == dividend:
            return 1
        if (dividend < 0 and divisor >= 0) or (dividend >=0 and divisor < 0):
            sign = False
        while n >= d:
            count = 0
            while n >= (d << (count + 1)):
                count +=1
            ans += (1 << count)
            n -= (d << count)
        if sign:
            if ans > 2** 31 -1 :
                return 2**31 - 1
        if not sign :
            ans = ans * -1
            if ans < - 2**31:
                return -2** 31
        return ans



        
        
        