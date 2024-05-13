# Revisit: 1 [1]
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

