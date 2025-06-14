# Revisit: 1 – 09/02/2025
# Revisit: 2 – 12/06/2025
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)
