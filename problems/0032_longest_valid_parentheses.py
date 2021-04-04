"""
Solution of the hard problem - "Longest Valid Parentheses",
https://leetcode.com/problems/longest-valid-parentheses/
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

