# Revisit: 2 – 10/02/2024
# Revisit: 1 – 12/06/2025
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)