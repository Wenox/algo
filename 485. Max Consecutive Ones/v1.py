# Revisit: 1 [1]
import this
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0
        for n in nums:
            cur_count = cur_count + 1 if n == 1 else 0
            max_count = max(max_count, cur_count)

        return max_count