# Revisit: 3 –– 16/02/2024
# Revisit: 3 –– 07/08/2025
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0