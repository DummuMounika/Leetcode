class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:  
            if token == '+' or token == '-' or token == '*' or token == '/':
                prevN2 = stack.pop()
                prevN1 = stack.pop()
                if token == '+':
                    stack.append(prevN1 + prevN2)
                elif token == '-':
                    stack.append(prevN1 - prevN2)
                elif token == '*':
                    stack.append(prevN1 * prevN2)
                elif token == '/':
                    stack.append(int(float(prevN1)/ prevN2))
            else:
                stack.append(int(token))

        return stack.pop()






        