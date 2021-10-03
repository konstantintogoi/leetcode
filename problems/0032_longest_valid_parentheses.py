"""
Solution of the hard problem
https://leetcode.com/problems/longest-valid-parentheses/
"Longest Valid Parentheses"
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """Longest Valid Parentheses.

        >>> Solution().longestValidParentheses('(()')
        2
        >>> Solution().longestValidParentheses(')()())')
        4
        >>> Solution().longestValidParentheses('')
        0

        """
        stack, ans = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans
