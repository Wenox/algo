# Revisit: 1
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
