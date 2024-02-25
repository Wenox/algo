class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_at_index = {}
        left, max_length = 0, 0
        for right in range(len(s)):
            if s[right] in seen_at_index:
                left = max(left, seen_at_index[s[right]])
            seen_at_index[s[right]] = right + 1
            max_length = max(max_length, 1 + right - left)

        return max_length