#LC 1652

#Solution:

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        if k>0 :
            win_sum = sum(code[1:k+1])
            for i in range(len(code)):
                ans[i] = win_sum
                win_sum -= code[(i+1)%n]
                win_sum += code[(i+k+1)%n]
            return ans
        else:
            k = abs(k)
            win_sum = sum(code[n-k:n])
            for i in range(len(code)):
                ans[i] = win_sum
                win_sum -= code[(i-k)%n]
                win_sum += code[(i)%n]
            return ans
            
        