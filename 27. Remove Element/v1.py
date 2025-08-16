# Revisit: 2 –– 19/02/2024
# Revisit: 2 –– 07/08/2025

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_to_value = {}
        k = 0
        for n in nums:
            if n != val:
                index_to_value[k] = n
                k += 1

        for i, v in index_to_value.items():
            nums[i] = v

        return k

