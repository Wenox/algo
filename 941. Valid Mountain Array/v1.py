# Revisit: 2
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        if arr[1] < arr[0]:
            return False

        peaked = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False

            if peaked:
                if arr[i] > arr[i - 1]:
                    return False
            else:
                if arr[i] < arr[i - 1]:
                    peaked = True

        return peaked
