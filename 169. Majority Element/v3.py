from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        result = None
        for n in nums:
            if majority == 0:
                result = n

            if result == n:
                majority += 1
            else:
                majority -= 1

        return result
