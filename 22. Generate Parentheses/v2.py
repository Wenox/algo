from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate_possible_parentheses(n, "", 0, 0)

    def generate_possible_parentheses(self, n: int, acc: str, open_count: int, close_count: int) -> List[str]:
        if len(acc) == 2 * n:
            return [acc]
        result = []
        if open_count < n:
            result += self.generate_possible_parentheses(n, acc + '(', open_count + 1, close_count)
        if close_count < open_count:
            result += self.generate_possible_parentheses(n, acc + ')', open_count, close_count + 1)
        return result