#LC 22. Generate Parentheses
#CODE:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res = []
        def backtrack(close,open):
            if close == open == n:
                res.append("".join(stack))
                return 
            if open < n:
                stack.append("(")
                backtrack(close,open+1)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(close+1,open)
                stack.pop()
        backtrack(0,0)
        return res



        