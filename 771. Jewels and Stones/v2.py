class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsMask = [False] * 52
        jewelsCount = [0] * 52
        for jewel in jewels:
            if ord(jewel) <= 90:
                jewelsMask[ord(jewel) - 65] = True
            else:
                jewelsMask[ord(jewel) - 71] = True

        for stone in stones:
            if ord(stone) <= 90:
                if jewelsMask[ord(stone) - 65]:
                    jewelsCount[ord(stone) - 65] += 1
            else:
                if jewelsMask[ord(stone) - 71]:
                    jewelsCount[ord(stone) - 71] += 1

        return sum(jewelsCount)