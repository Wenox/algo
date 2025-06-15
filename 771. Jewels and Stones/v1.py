# Revisit: 1 – 11/02/2024
# Revisit: 2 – 14/06/2025
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in set(jewels) for stone in stones)
