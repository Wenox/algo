from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        nums_sorted = [[] for _ in range(1 + len(nums))]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num, count in freq.items():
            nums_sorted[count].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for num in nums_sorted[i]:
                result.append(num)
            if (k == len(result)):
                return result