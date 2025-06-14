# Revisit: 2 – 11/02/2025
# Revisit: 2 – 13/06/2025
# Notes
# Tricky part: task says "division towards zero"
# But in Python:
# -121 // 7 = -18 (-17.2857)
# And in Java or C++:
# Java: -121 / 7 = -17 (-17.2857)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b), # truncate division towards zero!
            "*": lambda a, b: a * b
        }

        stack = []

        for token in tokens:
            if token in operations:
                op2, op1 = stack.pop(), stack.pop()
                v = operations[token](op1, op2)
                stack.append(v)
            else:
                stack.append(int(token))

        return stack.pop()
