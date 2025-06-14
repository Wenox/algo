from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        output = 0
        for num in nums:
            seen[num] = seen.get(num, -1) + 1
            output += seen[num]
        return output