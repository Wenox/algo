# Revisit: 1
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [""] * n
        for i in range (1, n + 1):
            r = ""
            if i % 3 == 0:
                r = "Fizz"
            if i % 5 == 0:
                r += "Buzz"
            if not r:
                r = str(i)
            result[i - 1] = r
        return result