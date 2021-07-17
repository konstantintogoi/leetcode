"""
Solution of the medium problem - "Palindromic Substrings",
https://leetcode.com/problems/palindromic-substrings/
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        """Palindromic Substrings.

        >>> Solution().countSubstrings('abc')
        3
        >>> Solution().countSubstrings('aaa')
        6

        """
        cnt = 0
        memo = {}
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if self.isPalindrome(s, i, j, memo):
                    cnt += 1
        return cnt

    def isPalindrome(self, s: str, i, j, memo: dict) -> bool:
        if i == j - 1:
            memo[i, j] = True
        elif i == j - 2:
            memo[i, j] = s[i] == s[j - 1]
        elif (i, j) not in memo and s[i] == s[j - 1]:
            memo[i, j] = self.isPalindrome(s, i + 1, j - 1, memo)
        elif (i, j) not in memo:
            memo[i, j] = False

        return memo[i, j]

