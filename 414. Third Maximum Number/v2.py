from typing import List

from sortedcontainers import SortedSet


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = SortedSet()
        for n in nums:
            seen.add(n)

        if len(seen) >= 3:
            return seen[-3]
        else:
            return max(seen)