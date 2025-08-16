# Revisit: 1 –– 13/02/2024
# Revisit: 2 –– 30/06/2025
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
