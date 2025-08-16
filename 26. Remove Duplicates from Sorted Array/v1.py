# Revisit: 2 –– 18/02/2024
# Revisit: 1 –– 07/08/2025
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1