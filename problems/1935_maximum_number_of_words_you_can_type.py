"""
Solution of the easy problem
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
"Maximum Number of Words You Can Type"
"""
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """Return the number of words in `text` you can full type.

        >>> Solution().canBeTypedWords('hello world', 'ad')
        1
        >>> Solution().canBeTypedWords('leet code', 'lt')
        1
        >>> Solution().canBeTypedWords('leet code', 'e')
        0

        """
        brletters = set(brokenLetters)
        brwordscnt = 0
        wordscnt = 0

        for hword in map(set, text.split()):
            wordscnt += 1
            if hword.intersection(brletters):
                brwordscnt += 1

        return wordscnt - brwordscnt

