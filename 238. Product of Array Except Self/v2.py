from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        output[0] = 1
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        mult = 1
        for i in reversed(range(n)):
            output[i] *= mult
            mult *= nums[i]

        return output