# Revisit: 3 – 11/02/2025
# Revisit: 2 – 11/06/2025
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in brackets:
                if not stack or stack.pop() != brackets[c]:
                    return False
            else:
                stack.append(c)

        return not bool(stack)