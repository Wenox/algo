# Revisit: 1 –– 11/02/2024
# Revisit: 1 –– 14/06/2025
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for oper in operations:
            if oper[1] == '+':
                X += 1
            else:
                X -= 1
        return X

