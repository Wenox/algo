# Revisit: 2
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])

        # check rows
        for row in board:
            numbers = list(filter(lambda c: c != '.', row))
            if len(numbers) != len(set(numbers)):
                return False

        # check columns
        for col in range(n):
            numbers = set()
            for row in range(n):
                v = board[row][col]
                if v != '.' and v in numbers:
                    return False
                else:
                    numbers.add(v)

        # check 3x3 sub-boxes
        for w in range(3):
            for h in range(3):
                numbers = set()
                for i in range(3):
                    for j in range(3):
                        v = board[i + 3 * w][j + 3 * h]
                        if v != '.' and v in numbers:
                            return False
                        else:
                            numbers.add(v)

        return True

