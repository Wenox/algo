# Revisit: 1 [1]
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest = 0
        for account in accounts:
            total = sum(account)
            wealthiest = max(wealthiest, total)
        return wealthiest