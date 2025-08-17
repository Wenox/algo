# O(log n)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        def divide(n):
            if n == 1:
                return True

            # Check if last bit is set
            if n & 1:
                return False

            # Divide by 2
            return divide(n >> 1)

        return divide(n)

