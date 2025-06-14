import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenOnce = {letter: False for letter in 'abcdefghijklmnopqrstuvwxyz'}

        for c in s:
            if c in seenOnce:
                seenOnce[c] = False
            else:
                seenOnce[c] = True

        for i, c in enumerate(s):
            if seenOnce[c]:
                return i

        return -1
