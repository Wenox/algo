# Revisit: 2 –– 30/06/2025

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboardMap = {key: index for index, key in enumerate(keyboard)}

        total, curr_index = 0, 0
        for c in word:
            target_index = keyboardMap[c]
            total += abs(target_index - curr_index)
            curr_index = target_index

        return total
