# Revisit: 1 [1]
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in reversed(range(len(arr))):
            v = arr[i]
            arr[i] = greatest
            greatest = max(greatest, v)
        return arr
