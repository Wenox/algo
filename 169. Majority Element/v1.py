# Revisit: 2
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        majority_tuple = (nums[0], counts[nums[0]])
        for k, v in counts.items():
            if v > majority_tuple[1]:
                majority_tuple = (k, v)
        return majority_tuple[0]