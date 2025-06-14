# Revisit: 2 –– 12/06/2025

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenOnce = {letter: False for letter in string.ascii_lowercase}
        for i, c in enumerate(s):
            if c in seenAtIndex:
                seenAtIndex[c] = (False, i)
            else:
                seenAtIndex[c] = (True, i)

        minIndex = 10 ** 5 + 1
        for value in seenAtIndex.values():
            unique, index = value
            if unique:
                minIndex = min(minIndex, index)

        return -1 if minIndex == 10 ** 5 + 1 else minIndex



