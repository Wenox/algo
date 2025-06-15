# Revisit: 2 –– 12/02/2024
# Revisit: 1 –– 15/06/2025
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mappings = {}
        for i, n in enumerate(numbers, start=1):
            diff = target - n
            if diff in mappings:
                return sorted([i, mappings[diff]])
            else:
                mappings[n] = i
