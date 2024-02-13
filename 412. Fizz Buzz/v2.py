from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [""] * n
        mapping = {3: 'Fizz', 5: 'Buzz'}

        for i in range(1, n + 1):
            r = ""
            for k, v in mapping.items():
                if i % k == 0:
                    r += mapping[k]
            if not r:
                r = str(i)
            result[i - 1] = r

        return result
