# Revisit: 3 –– 12/02/2024
# Revisit: 2 –– 15/06/2025
#
#
#
# Notes: Interview Tip: Whenever you're trying to solve an array problem in place,
# always consider the possibility of iterating backwards instead of forwards through the array.
# It can completely change the problem, and make it a lot easier.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2:
            return

        index_to_value = {}
        i = 0
        l = 0
        r = 0
        while i < m + n and l < m and r < n:
            if nums1[l] < nums2[r]:
                index_to_value[i] = nums1[l]
                l += 1
            else:
                index_to_value[i] = nums2[r]
                r += 1
            i += 1

        if i < m + n:
            if not l < m:
                while i < m + n:
                    index_to_value[i] = nums2[r]
                    r += 1
                    i += 1
            else:
                while i < m + n:
                    index_to_value[i] = nums1[l]
                    l += 1
                    i += 1

        for i, v in index_to_value.items():
            nums1[i] = v