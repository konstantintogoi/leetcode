"""
Solution of the easy problem
https://leetcode.com/problems/coupon-code-validator/
"Coupon Code Validator"
"""
import re
from typing import List


regexp = re.compile('^[a-zA-Z0-9_]+$')
business_lines = {
    'electronics': 1,
    'grocery': 2,
    'pharmacy': 3,
    'restaurant': 4,
}


class Solution:
    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool],
    ) -> List[str]:
        """Return an array of the codes of all valid coupons.

        >>> Solution().validateCoupons(
        ...     ['SAVE20', '', 'PHARMA5', 'SAVE@20'],
        ...     ['restaurant', 'grocery', 'pharmacy', 'restaurant'],
        ...     [True, True, True, True],
        ... )
        ['PHARMA5', 'SAVE20']
        >>> Solution().validateCoupons(
        ...     ['GROCERY15', 'ELECTRONICS_50', 'DISCOUNT10'],
        ...     ['grocery', 'electronics', 'invalid'],
        ...     [False, True, True],
        ... )
        ['ELECTRONICS_50']
        >>> Solution().validateCoupons(
        ...     ['m', 'A', 'B', 'P', 'J', 'P', 'u', 'W', '4', 'J', 'C', '9'],
        ...     [
        ...         'electronics', 'invalid', 'invalid', 'pharmacy',
        ...         'invalid', 'electronics', 'restaurant', 'grocery',
        ...         'restaurant', 'pharmacy', 'pharmacy', 'pharmacy',
        ...     ],
        ...     [
        ...         True, True, False, True, False, True,
        ...         True, False, False, False, True, False,
        ...     ],
        ... )
        ['P', 'm', 'C', 'P', 'u']

        """
        valid_codes = []

        for i in range(len(code)):
            if not regexp.match(code[i]):
                continue
            if businessLine[i] not in business_lines:
                continue
            if not isActive[i]:
                continue

            valid_codes.append((businessLine[i], code[i]))

        sorted_codes = sorted(valid_codes)
        return [code for line, code in sorted_codes]

