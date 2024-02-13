# Revisit: 2
from typing import List


# Notes: in python no need to use "temp" for swap
# x, y = y, x
# Also, arr[~i] = arr[-1-i] = arr[n - i - i]
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            l = 0
            r = n - 1
            while l <= r:
                if l < r:
                    row[l], row[r] = row[r] ^ 1, 1 - row[l]  ## Two ways to toggle a value: 1 - x or XOR
                elif l == r:
                    row[l] ^= 1
                l += 1
                r -= 1
        return image





