# Revisit: 1
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda s: len(s) % 2 == 0, map(str, nums))))
