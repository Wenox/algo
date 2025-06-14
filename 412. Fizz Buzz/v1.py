# Revisit: 1 – 13/02/2024
# Revisit: 1 – 20/05/2024
# Revisit: 2 – 10/06/2025
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