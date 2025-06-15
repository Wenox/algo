# Revisit: 3 –– 10/02/2024
# Revisit: 1 –– 15/06/2025
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            grouped_anagrams[key].append(word)

        return list(grouped_anagrams.values())
