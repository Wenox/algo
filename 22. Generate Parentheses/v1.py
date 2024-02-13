# Revisit: 3
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parantheses_list = self.generate_possible_parantheses(n, [], "")
        result = []
        for parantheses in parantheses_list:
            c = 0
            for p in parantheses:
                if p == '(':
                    c += 1
                else:
                    c -= 1

                if c < 0:
                    break

            if c == 0:
                result.append(parantheses)

        return result

    def generate_possible_parantheses(self, n: int, result: List[str], acc: str) -> List[str]:
        if len(acc) == (2 * n):
            result.append(acc)
            return result
        else:
            self.generate_possible_parantheses(n, result, acc + '(')
            self.generate_possible_parantheses(n, result, acc + ')')
        return result
