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
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []

        for token in tokens:
            if token in operations:
                op2 = stack.pop()
                op1 = stack.pop()
                v = operations[token](op1, op2)
                stack.append(v)
            else:
                stack.append(int(token))
        return stack.pop()
