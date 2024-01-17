class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        # Create the regular stack and a stack that will track the min at that respective index

    def push(self, val):
        self.stack.append(val)
        if len(self.minStack) != 0:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            self.minStack.append(val)

        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.stack.pop(-1)
        self.minStack.pop(-1)
        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.minStack[-1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()