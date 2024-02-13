from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(count_left, count_right):
            if n == count_left == count_right:
                result.append("".join(stack))
                return

            if count_left < n:
                stack.append("(")
                backtrack(count_left + 1, count_right)
                stack.pop()

            if count_right < count_left:
                stack.append(")")
                backtrack(count_left, count_right + 1)
                stack.pop()

        backtrack(0, 0)
        return result
