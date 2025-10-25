"""
Solution of the medium problem
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"Evaluate Reverse Polish Notation"
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Return an integer that represents the value of the expression.

        >>> Solution().evalRPN(['2', '1', '+', '3', '*'])
        9
        >>> Solution().evalRPN(['4', '13', '5', '/', '+'])
        6
        >>> Solution().evalRPN([
        ...     '10', '6', '9', '3', '+',
        ...     '-11', '*', '/', '*',
        ...     '17', '+', '5', '+',
        ... ])
        22

        """
        args = []

        for token in tokens:
            if token == '+':
                b = args.pop()
                a = args.pop()
                args.append(a + b)
            elif token == '-':
                b = args.pop()
                a = args.pop()
                args.append(a - b)
            elif token == '*':
                b = args.pop()
                a = args.pop()
                args.append(a * b)
            elif token == '/':
                b = args.pop()
                a = args.pop()
                args.append(int(a / b))
            else:
                args.append(int(token))

        return args[0]

