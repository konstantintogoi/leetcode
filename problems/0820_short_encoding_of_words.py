"""
Solution of the medium problem
https://leetcode.com/problems/short-encoding-of-words/
"Short Encoding of Words"
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """Short Encoding.

        >>> Solution().minimumLengthEncoding(['time', 'me', 'bell'])
        10
        >>> Solution().minimumLengthEncoding(['t'])
        2
        >>> Solution().minimumLengthEncoding(['me', 'time'])
        5
        >>> Solution().minimumLengthEncoding(['time', 'atime', 'btime'])
        12

        """
        curword = ''
        encword = ''
        words.sort(key=lambda x: -len(x))
        for word in words:
            curword = word + '#'
            if curword in encword:
                continue
            else:
                encword += curword
        return len(encword)
