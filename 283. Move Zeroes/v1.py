# Revisit: 1.5 –– 08/08/2025
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        seen_zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                seen_zeroes += 1
            else:
                nums[i - seen_zeroes] = nums[i]

        for i in range(len(nums) - seen_zeroes, len(nums)):
            nums[i] = 0