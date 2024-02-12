from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mappings = {}
        for i, n in enumerate(numbers, start=1):
            diff = target - n
            if diff in mappings:
                return sorted([i, mappings[diff]])
            else:
                mappings[n] = i
