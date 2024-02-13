from itertools import accumulate
from typing import List


class Solution:
    def adding_two(self, a: int, b: int) -> int:
        return a + b

    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums, self.adding_two))
