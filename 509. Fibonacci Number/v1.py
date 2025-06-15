# Revisit: 3 –– 12/02/2024
# Revisit: 2 –– 15/06/2025
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
