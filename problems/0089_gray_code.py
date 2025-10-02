"""
Solution of the medium problem
https://leetcode.com/problems/gray-code/
"Gray Code"
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """Return any valid n-bit gray code sequence.

        >>> Solution().grayCode(2)
        [0, 1, 3, 2]
        >>> Solution().grayCode(1)
        [0, 1]
        >>> Solution().grayCode(3)
        [0, 1, 3, 2, 6, 7, 5, 4]


        """
        nums = {i for i in range((1 << n) - 1, 0, -1)}

        greycode = [0]
        self.backtrack(0, nums, greycode)
        return greycode

    def backtrack(self, prevnum, nums, gc) -> List[int]:
        for i in range(prevnum.bit_length() + 1):
            num = (1 << i) ^ prevnum
            if num not in nums:
                continue

            gc.append(num)
            nums.remove(num)

            if not nums:
                return gc
            if self.backtrack(num,nums,gc) and (gc[0]^gc[-1]).bit_count()==1:
                return gc

            nums.add(num)
            gc.pop()

