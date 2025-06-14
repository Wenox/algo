# Revisit: 2 – 11/02/2024
# Revisit: 2 – 11/06/2025
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
