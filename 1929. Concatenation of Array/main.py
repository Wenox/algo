from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        concatenated = [0] * 2 * size
        for i, n in enumerate(nums):
            concatenated[i] = n
            concatenated[i + size] = n
        return concatenated
