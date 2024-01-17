class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(float(num2) / num1))
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            else:
                stack.append(int(token)) 

        return stack[0]

        """
        :type tokens: List[str]
        :rtype: int
        """
        