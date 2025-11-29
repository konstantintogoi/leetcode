"""
Solution of the easy problem
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"Replace Elements with Greatest Element on Right Side"
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """Replace every element in `arr` with the greatest element.

        >>> Solution().replaceElements([17, 18, 5, 4, 6, 1])
        [18, 6, 6, 6, 1, -1]
        >>> Solution().replaceElements([400])
        [-1]

        """
        m = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            num = arr[i]
            arr[i] = m
            m = max(num, m)
        return arr

