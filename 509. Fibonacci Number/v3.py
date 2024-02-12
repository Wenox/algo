class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            saved = [0, 1]
            for i in range(2, n + 1):
                saved.append(saved[i - 2] + saved[i - 1])
            return saved[-1]
