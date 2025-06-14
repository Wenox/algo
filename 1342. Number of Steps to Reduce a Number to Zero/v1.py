# Revisit: 2 – 13/02/2024
# Revisit: 2 – 10/06/2025
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1 == 0:
                num >>= 1
            else:
                num &= ~1
            steps += 1
        return steps

