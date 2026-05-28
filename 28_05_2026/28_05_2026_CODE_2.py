#150. Evaluate Reverse Polish Notation
#CODE:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                if i == '+':
                    el1=stack.pop()
                    el2 = stack.pop()
                    res= int(el1) + int(el2)
                    stack.append(res)
                if i == '-':
                    el1=stack.pop()
                    el2 = stack.pop()
                    res= int(el2) - int(el1)
                    stack.append(res)
                if i == '*':
                    el1=stack.pop()
                    el2 = stack.pop()
                    res= int(el1) * int(el2)
                    stack.append(res)
                if i == '/':
                    el1=stack.pop()
                    el2 = stack.pop()
                    res= int(el2) / int(el1)
                    stack.append(res)
        if not stack:
            return 0
        return int(stack[0])

                