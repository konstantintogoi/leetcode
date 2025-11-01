"""
Solution of the medium problem
https://leetcode.com/problems/product-of-array-except-self/
"Product of Array Except Self"
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Return an array, s.t. `answer[i]` is equal to the product.

        >>> Solution().productExceptSelf([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> Solution().productExceptSelf([-1, 1, 0, -3, 3])
        [0, 0, 9, 0, 0]

        """
        n = len(nums)

        lproducts = [1]
        for num in nums:
            lproducts.append(lproducts[-1] * num)

        rproducts = [1]
        for i in range(n - 1, -1, -1):
            rproducts.append(rproducts[-1] * nums[i])

        products = []

        for i in range(1, n + 1):
            lproduct = lproducts[i - 1]
            rproduct = rproducts[n - i]
            products.append(lproduct * rproduct)

        return products

