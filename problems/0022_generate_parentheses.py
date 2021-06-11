"""
Solution of the medium problem - "Generate Parentheses",
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[int]:
        """Generate Parentheses.

        >>> Solution().generateParenthesis(1)
        ['()']
        >>> Solution().generateParenthesis(2)
        ['(())', '()()']
        >>> Solution().generateParenthesis(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']

        """
        def dp(m, memo=None):
            memo = memo or {0: [], 1: ['()'], 2: ['(())', '()()']}
            if m not in memo:
                pars = []
                for i in range(m, 0, -1):
                    inner_pars = dp(i - 1, memo)
                    other_pars = dp(m - i, memo)
                    if not other_pars:
                        pars.extend(['(' + p + ')' for p in inner_pars])
                        continue
                    if not inner_pars:
                        pars.extend(['()' + p for p in other_pars])
                        continue
                    for pleft in inner_pars:
                        for pright in other_pars:
                            pars.append('(' + pleft + ')' + pright)

                memo[m] = pars
            return memo[m]

        return dp(n)

