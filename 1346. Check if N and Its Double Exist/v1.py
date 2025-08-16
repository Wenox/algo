# Revisit: 1 –– 18/02/2024
# Revisit: 1 –– 30/06/2025
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if n % 2 == 0 and n / 2 in seen:
                return True
            if n * 2 in seen:
                return True
            seen.add(n)

        return False
