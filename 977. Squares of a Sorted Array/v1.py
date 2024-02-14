# Revisit: 1
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        i = len(nums) - 1
        output = [None] * len(nums)
        for n in nums:
            if abs(nums[l]) > abs(nums[r]):
                output[i] = nums[l] * nums[l]
                l += 1
            else:
                output[i] = nums[r] * nums[r]
                r -= 1
            i -= 1
        return output

