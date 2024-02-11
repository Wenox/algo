from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [count_tuple[0] for count_tuple in Counter(nums).most_common(k)]
