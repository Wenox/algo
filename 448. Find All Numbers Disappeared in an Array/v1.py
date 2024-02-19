# Revisit: 2
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = [False] * len(nums)
        for n in nums:
            seen[n - 1] = True

        result = []
        for i, v in enumerate(seen):
            if not v:
                result.append(i + 1)

        return result
