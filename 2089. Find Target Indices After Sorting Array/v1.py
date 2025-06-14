# Revisit: 2 –– 14/06/2025
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counted_target = 0
        counted_smaller = 0
        for n in nums:
            if n < target:
                counted_smaller += 1
            elif n == target:
                counted_target += 1

        return [i for i in range(counted_smaller, counted_smaller + counted_target)]