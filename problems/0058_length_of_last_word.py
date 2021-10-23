"""
Solution of the easy problem
https://leetcode.com/problems/length-of-last-word/
"Length of Last Word"
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Length of Last Word.

        >>> Solution().lengthOfLastWord('Hello World')
        5
        >>> Solution().lengthOfLastWord(' ')
        0
        >>> Solution().lengthOfLastWord('a ')
        1
        >>> Solution().lengthOfLastWord('a')
        1
        >>> Solution().lengthOfLastWord('b  a   ')
        1

        """
        start = stop = lastlen = 0

        for i, c in enumerate(s):
            if c != ' ':
                if start == stop:
                    lastlen = 0
                stop += 1
                lastlen += 1
            else:
                if stop - start:
                    lastlen = stop - start
                start, stop = i, i

        return lastlen
