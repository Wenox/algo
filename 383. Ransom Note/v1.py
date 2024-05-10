# Revisit: 1 [1]
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = defaultdict(int)
        for c in magazine:
            counts[c] += 1

        for c in ransomNote:
            if counts[c] == 0:
                return False
            else:
                counts[c] -= 1

        return True
