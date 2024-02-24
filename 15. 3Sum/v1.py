# Revisit: 3
# https://en.wikipedia.org/wiki/3SUM
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set([])
        for i in range(0, len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result


