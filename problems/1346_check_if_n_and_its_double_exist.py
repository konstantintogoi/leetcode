"""
Solution of the easy problem
https://leetcode.com/problems/check-if-n-and-its-double-exist/
"Check If N and Its Double Exist"
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """Check if there exist two indices `i` and `j` s.t. `a[i]==2*a[j]`.

        >>> Solution().checkIfExist([10, 2, 5, 3])
        True
        >>> Solution().checkIfExist([3, 1, 7, 11])
        False
        >>> Solution().checkIfExist([0, -2, 2])
        False
        >>> Solution().checkIfExist([0, 0])
        True

        """
        ints = set()
        halfs = set()
        doubles = set()
        nzeros = 0

        for num in arr:
            ints.add(num)
            if num % 2:
                doubles.add(num * 2)
            elif num == 0:
                nzeros += 1
            else:
                halfs.add(num / 2)

        return (
            bool(ints.intersection(doubles)) or
            bool(ints.intersection(halfs)) or
            nzeros > 1
        )

