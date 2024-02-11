from collections import deque

# Naive approach (pop is not O(1))
class MinStack:

    def __init__(self):
        self.min = 0
        self.deque = deque()

    def push(self, val: int) -> None:
        if not self.deque or val < self.min:
            self.min = val
        self.deque.append(val)

    def pop(self) -> None:
        popped = self.deque.pop()
        if popped == self.min and self.deque:
            new_min = self.deque[0]
            for v in self.deque:
                if v < new_min:
                    new_min = v
            self.min = new_min

    def top(self) -> int:
        return self.deque[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()