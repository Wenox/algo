from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -2**31
        seen = set()
        for n in nums:
            if n in seen:
                continue
            seen.add(n)

            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n

        if len(seen) >= 3:
            return third
        else:
            return first