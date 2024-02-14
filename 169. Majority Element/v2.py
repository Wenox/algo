from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
            if counts[n] > len(nums) // 2:
                return n
