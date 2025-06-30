# Revisit: 1 –– 11/02/2024
# Revisit: 1 –– 30/06/2025
class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join(c for c in s if c not in {'a', 'e', 'i', 'o', 'u'})
