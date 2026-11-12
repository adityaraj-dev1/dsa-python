"""
Problem: Evaluate Reverse Polish Notation
LeetCode: 150

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                elif token == "/":
                    result = abs(a) // abs(b)

                    if (a < 0) != (b < 0):
                        result = -result

                    stack.append(result)

        return stack[-1]