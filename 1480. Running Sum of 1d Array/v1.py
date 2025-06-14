# Revisit: 1 – 13/02/2024
# Revisit: 1 – 13/05/2024
# Revisit: 1 – 10/06/2025
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
