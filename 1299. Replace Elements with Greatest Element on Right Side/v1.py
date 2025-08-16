# Revisit: 1 –– 18/02/2024
# Revisit: 2.5 –– 07/08/2025
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in reversed(range(len(arr))):
            v = arr[i]
            arr[i] = greatest
            greatest = max(greatest, v)
        return arr
