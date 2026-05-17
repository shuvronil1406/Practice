#LC 20. Valid Parentheses
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#CODE: 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top=-1
        pairs ={
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        for i in s:
            if i in pairs.keys():
                stack.append(i)
                top+=1
            else:
                if not stack:
                    return False
                if pairs[stack[top]] == i:
                    # stack.pop()
                    top-=1
                    stack.pop()
                else:
                    return False
        return len(stack)==0 