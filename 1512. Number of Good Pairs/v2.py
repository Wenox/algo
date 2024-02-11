from collections import Counter
from math import comb
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(comb(count, 2) for count in Counter(nums).values())