# Revisit: 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length, curr_length = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in seen:
                    curr_length = 0
                    seen.clear()
                    break
                else:
                    curr_length += 1
                    seen.add(s[j])
                    max_length = max(curr_length, max_length)

        return max_length
