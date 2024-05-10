# Revisit: 1 [1]
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101
        for height in heights:
            counts[height] += 1

        expected = []
        for height, count in enumerate(counts):
            if count != 0:
                same_height_people = [height] * count
                expected.extend(same_height_people)

        diff = 0
        for h1, h2 in zip(heights, expected):
            if h1 != h2:
                diff += 1
