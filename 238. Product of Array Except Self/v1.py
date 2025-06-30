# Revisit: 3 – 12/02/2024
# Revisit: 3 – 22/06/2025
# What if there are 0s in the array?
# -> If one zero, then 0s and arr[non-zero] = product of others
# -> If two zeros: everything is 0
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [1] * n, [1] * n
        for i in range (1, n):
            l[i] = l[i - 1] * nums[i - 1]
            r[n - i - 1] = r[n - i] * nums[n - i]
        return [l[i] * r[i] for i in range(n)]

