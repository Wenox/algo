# Revisit: 3
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [1] * n, [1] * n
        for i in range (1, n):
            l[i] = l[i - 1] * nums[i - 1]
            r[n - i - 1] = r[n - i] * nums[n - i]
        return [l[i] * r[i] for i in range(n)]

