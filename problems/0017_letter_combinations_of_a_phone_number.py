"""
Solution of "Letter Combinations of a Phone Number" problem at
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Letter Combinations.

        >>> Solution().letterCombinations('23')
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> Solution().letterCombinations('')
        []
        >>> Solution().letterCombinations('2')
        ['a', 'b', 'c']

        """
        n = len(digits)
        if n == 0:
            return []

        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        if n == 1:
            return letters[digits[0]]

        combs = []

        for l in letters[digits[0]]:
            for c in self.letterCombinations(digits[1:]):
                combs.append(l + c)

        return combs

