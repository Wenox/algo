class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = left = right = 0
        while right < len(s):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                right += 1
                max_length = max(max_length, right - left)

        return max_length
