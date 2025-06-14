# Revisit: 1 – 13/02/2024
# Revisit: 1 – 10/05/2024
# Revisit: 1 – 10/06/2025
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))