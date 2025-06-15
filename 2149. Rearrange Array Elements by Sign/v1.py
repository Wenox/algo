# Revisit: 1 –– 10/02/2024
# Revisit: 1 –– 15/06/2025
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = 0, 1
        result = nums[:]
        for num in nums:
            if num >= 0:
                result[positive] = num
                positive += 2
            else:
                result[negative] = num
                negative += 2
        return result
