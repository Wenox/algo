from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Compute prefix products
        # Input: [1, 2, 3, 4, 5]
        # Computed: [1, 1, 2, 6, 24]
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]

        # Handle suffix products
        # [120, 60, 40, 30, 24]
        acc = nums[n - 1]
        for i in range(n - 2, -1, -1):
            answer[i] = answer[i] * acc
            acc = acc * nums[i]

        return answer
