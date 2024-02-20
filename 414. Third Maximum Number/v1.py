# Revisit: 2
from heapq import heappop, heappush
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        kth_max = 3
        heap = []
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)

            if len(heap) == kth_max:
                if heap[0] < num:
                    heappop(heap)
                    heappush(heap, num)
            else:
                heappush(heap, num)

        if len(heap) == kth_max:
            return heap[0]
        else:
            return max(heap)