"""
Solution of the medium problem - "Find K Closest Elements",
https://leetcode.com/problems/find-k-closest-elements/
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Closest Elements.

        >>> Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)
        [1, 2, 3, 4]
        >>> Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1)
        [1, 2, 3, 4]
        >>> Solution().findClosestElements([-2, -1, 1, 2, 3, 4, 5], 7, 3)
        [-2, -1, 1, 2, 3, 4, 5]

        """
        l, r = -1, len(arr)

        while l + 1 != r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid
            else:
                r = mid

        if l == -1: return arr[:k]
        if r == len(arr): return arr[-k:]

        ans = []
        while l > -1 or r < len(arr):
            a = arr[l] if l > -1 else float('inf')
            b = arr[r] if r < len(arr) else float('inf')

            if abs(a - x) <= abs(b - x):
                ans.insert(0, a)
                l -= 1
            else:
                ans.append(b)
                r += 1

            if len(ans) == k:
                return ans

        return ans

