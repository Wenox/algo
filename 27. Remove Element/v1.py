# Revisit: 2

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

