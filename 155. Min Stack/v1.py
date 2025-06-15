# Revisit: 2 –– 11/02/2025
# Revisit: 2 –– 14/06/2025
# Naive approach (pop is not O(1))
class MinStack:

    def __init__(self):
        self.min = 0
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min and self.stack:
            new_min = self.stack[0]
            for v in self.stack:
                if v < new_min:
                    new_min = v
            self.min = new_min

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()