"""
Solution of "Multiply Strings" problem at
https://leetcode.com/problems/multiply-strings/
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Multiply Strings.

        >>> Solution().multiply('2', '3')
        '6'
        >>> Solution().multiply('123', '456')
        '56088'
        >>> Solution().multiply('111', '3')
        '333'
        >>> Solution().multiply('4', '222')
        '888'
        >>> Solution().multiply('18', '7')
        '126'
        >>> Solution().multiply('9133', '0')
        '0'

        """
        if num1 == '0' or num2 == '0': return '0'

        n, m = len(num1), len(num2)
        nums1 = [ord(c) - ord('0') for c in num1]
        nums2 = [ord(c) - ord('0') for c in num2]
        mult = ''

        j, digit = m - 1, 0
        while 0 <= j or digit:
            b = 0 if j < 0 else nums2[j]

            i, addend = n - 1, '0' * (m - j - 1)
            while 0 <= i or digit:
                a = 0 if i < 0 else nums1[i]

                digit += a * b
                addend = str(digit % 10) + addend
                digit = digit // 10
                i -= 1

            mult = self.add(mult, addend)
            j -= 1

        return mult

    def add(self, num1: str, num2: str) -> str:
        """Add.

        >>> Solution().add('2', '3')
        '5'
        >>> Solution().add('111', '222')
        '333'
        >>> Solution().add('99', '1')
        '100'
        >>> Solution().add('999', '0')
        '999'
        >>> Solution().add('0', '999')
        '999'

        """
        if num1 == '0': return num2
        if num2 == '0': return num1

        n, m = len(num1), len(num2)
        summ = ''

        i, j, digit = n - 1, m - 1, 0
        while 0 <= i or 0 <= j or digit:
            digit += 0 if i < 0 else int(num1[i])
            digit += 0 if j < 0 else int(num2[j])
            summ = str(digit % 10) + summ
            digit = 1 if digit > 9 else 0
            i -= 1
            j -= 1

        return summ

