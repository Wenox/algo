# Notes
# Tricky part: '<=' sign: because min values should be repeated
# For instance, when inserting these values: [0, 5, 8, 5]
# The min stack must become: [0, 5, 5] and not [0, 5]
##
##
# This approach can be further optimised by storing pairs in the min_stack,
# where the second value of the pair represents the number of repeated occurences:
# Values: [0, 5, 8, 5]
# Min stack: [(0, 1), (5, 2)]
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()