"""
Solution of the easy problem
https://leetcode.com/problems/add-binary/
"Add Binary"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Add Binary.

        >>> Solution().addBinary('11', '1')
        '100'
        >>> Solution().addBinary('1010', '1011')
        '10101'

        """
        i, bit, s = 0, 0, ''

        while bit or i < len(a) or i < len(b):
            x = int(a[len(a) - i - 1]) if i < len(a) else 0
            y = int(b[len(b) - i - 1]) if i < len(b) else 0
            bit = x + y + bit
            s = str(bit % 2) + s
            bit = bit // 2
            i += 1

        return s
