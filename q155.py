class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.a.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.a)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()