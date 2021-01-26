"""
Solution of "Max Difference You Can Get From Changing an Integer" problem at
https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
"""
class Solution:
    def maxDiff(self, num: int) -> int:
        """Max Difference You Can Get From Changing an Integer.

        >>> Solution().maxDiff(555)
        888
        >>> Solution().maxDiff(9)
        8
        >>> Solution().maxDiff(123456)
        820000
        >>> Solution().maxDiff(10000)
        80000
        >>> Solution().maxDiff(9288)
        8700
        >>> Solution().maxDiff(6919862)
        8000080

        """
        tmp = num
        bit_order = 0
        first_digit = True
        for i in range(8, -1, -1):
            base = 10 ** i
            digit = int(tmp / base)
            tmp -= base * digit
            if digit or bit_order:
                bit_order = bit_order or i
                digit_num = i
                if digit == 9:
                    first_digit = False
                    continue
                else:
                    break

        a = 0
        tmp = num
        for i in range(bit_order + 1):
            div = tmp % 10
            tmp = int(tmp / 10)
            if div == digit:
                a += 9 * (10 ** i)
            else:
                a += div * (10 ** i)

        tmp = num
        bit_order = 0
        first_digit = True
        for i in range(8, -1, -1):
            base = 10 ** i
            digit = int(tmp / base)
            tmp -= base * digit
            if digit:
                bit_order = bit_order or i
                digit_num = i
                if digit == 1:
                    first_digit = False
                    continue
                else:
                    break

        b = 0
        tmp = num
        subst = 1 if first_digit else 0
        for i in range(bit_order + 1):
            div = tmp % 10
            tmp = int(tmp / 10)
            if div == digit:
                b += subst * (10 ** i)
            else:
                b += div * (10 ** i)

        return a - b

