from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_numbers_count = 0
        for n in nums:
            if self.is_even_digits(n):
                even_numbers_count += 1
        return even_numbers_count

    def is_even_digits(self, n: int) -> bool:
        divisions_count = 0
        while n != 0:
            n //= 10
            divisions_count += 1
        return divisions_count % 2 == 0

