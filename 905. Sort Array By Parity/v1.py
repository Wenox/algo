# Revisit: 2 [1] {1}
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[odd], nums[i] = nums[i], nums[odd]
                odd += 1
        return nums