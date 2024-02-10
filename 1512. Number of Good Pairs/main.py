from math import comb
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1

        result = 0
        for count in frequency.values():
            result += comb(count, 2)

        return result