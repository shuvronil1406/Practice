#412. Fizz Buzz
#CODE:

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        L=[0] * n
        L[0] = "1"
        for i in range(2,n+1):
            if i%3 == 0 and i % 5 == 0:
                L[i-1] = "FizzBuzz"
            elif i%3 == 0:
                L[i-1] = "Fizz"
            elif i%5 == 0:
                L[i-1] = "Buzz"
            else:
                L[i-1] = str(i)
        return L
        