# Revisit: 2 – 10/02/2024
# Revisit: 2 – 14/06/2025
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = nums[:]
        for i in range(n):
            result[i * 2] = nums[i]
            result[i * 2 + 1] = nums[n + i]
        return result