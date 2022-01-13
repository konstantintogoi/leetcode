"""
Solution of the medium problem
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"Remove All Adjacent Duplicates in String II"
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """Remove Duplicates.

        >>> Solution().removeDuplicates('abcd', 2)
        'abcd'
        >>> Solution().removeDuplicates('deeedbbcccbdaa', 3)
        'aa'
        >>> Solution().removeDuplicates('pbbcggttciiippooaais', 2)
        'ps'

        """
        if k == 1:
            return ''

        counter = [['', 1]]

        for char in s:
            if char == counter[-1][0]:
                counter[-1][1] += 1
            else:
                counter.append([char, 1])

            if counter[-1][1] == k:
                counter.pop()

        return ''.join([char * cnt for char, cnt in counter])
