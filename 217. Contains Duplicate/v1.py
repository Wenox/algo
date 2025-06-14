# Revisit: 1 – 09/02/2024
# Revisit: 1 – 10/06/2025
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
