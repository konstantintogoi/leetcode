"""
Solution of the medium problem - "ZigZag Conversion",
https://leetcode.com/problems/zigzag-conversion/
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """ZigZag Conversion.

        >>> Solution().convert('PAYPALISHIRING', 3)
        'PAHNAPLSIIGYIR'
        >>> Solution().convert('PAYPALISHIRING', 4)
        'PINALSIGYAHRPI'

        """
        a, s = [], [c for c in reversed(s)]

        while s:
            a.append([s.pop() if s else '' for _ in range(numRows)])

            if not s:
                break

            for i in range(numRows - 2, 0, -1):
                col = []
                for j in range(numRows):
                    col.append(s.pop() if i == j and s else '')
                a.append(col)

        s = ''
        for i in range(numRows):
            for j in range(len(a)):
                s += a[j][i]
        return s

