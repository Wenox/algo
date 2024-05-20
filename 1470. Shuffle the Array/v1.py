# Revisit: 2
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = nums[:]
        for i in range(n):
            result[i * 2] = nums[i]
            result[i * 2 + 1] = nums[n + i]
        return result