# Revisit: 1 –– 14/02/2024
# Revisit: 1 –– 30/06/2025
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda s: len(s) % 2 == 0, map(str, nums))))
