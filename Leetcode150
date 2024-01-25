class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(["+","-","/","*"])


        for token in tokens:
            if token not in op:
                stack.append(int(token))

            else: 
                op1 = stack.pop()
                op2 = stack.pop()

                if token == "+":
                    stack.append(op1 + op2 )
                if token == "-":
                    stack.append(op2 - op1)
                if token == "/":
                    if op2 == 0:
                        stack.append(0)  
                    else:
                        stack.append(int(op2 / op1))
                if token == "*":
                    stack.append(op1 * op2 )
            
        return stack[0]
            
