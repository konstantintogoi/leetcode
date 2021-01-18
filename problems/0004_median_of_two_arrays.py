"""
Solution of "Median of Two Sorted Arrays" problem at
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Median of Two Sorted Arrays.

        >>> Solution().findMedianSortedArrays([1, 3], [2])
        2
        >>> Solution().findMedianSortedArrays([1, 2], [3, 4])
        2.5
        >>> Solution().findMedianSortedArrays([0, 0], [0, 0])
        0.0
        >>> Solution().findMedianSortedArrays([], [1])
        1
        >>> Solution().findMedianSortedArrays([2], [])
        2
        >>> Solution().findMedianSortedArrays([1, 2], [1, 2])
        1.5
        >>> Solution().findMedianSortedArrays([1], [1])
        1.0
        >>> Solution().findMedianSortedArrays([1, 2], [1, 2, 3])
        2
        >>> Solution().findMedianSortedArrays([1], [2, 3, 4])
        2.5

        """
        n, m = len(nums1), len(nums2)

        if n == 1 and m == 1:
            return (nums1[0] + nums2[0]) / 2

        npm = n + m
        arr = [[0 for _ in range(m)] for _ in range(n)]
        mid = (n + m - 1) // 2

        if not nums1:
            if npm % 2:
                return nums2[mid]
            else:
                return (nums2[mid] + nums2[mid + 1]) / 2

        if not nums2:
            if npm % 2:
                return nums1[mid]
            else:
                return (nums1[mid] + nums1[mid + 1]) / 2

        for i in range(n):
            j = self.search(nums1[i], nums2, 0, m)
            if (j < m and nums1[i] == nums2[j]):
                j += 1
            if i + j == mid:
                if npm % 2:
                    return nums1[i]
                elif i + 1 < n and j < m:
                    return (nums1[i] + min(nums1[i + 1], nums2[j])) / 2
                elif i + 1 < n:
                    return (nums1[i] + nums1[i + 1]) / 2
                else:

                    return (nums1[i] + nums2[j]) / 2

        for j in range(m):
            i = self.search(nums2[j], nums1, 0, n)
            #if (i < n and nums1[i] == nums2[j]):
            #    i += 1
            if i + j == mid:
                if npm % 2:
                    return nums2[j]
                elif j + 1 < m and i < n:
                    return (nums2[j] + min(nums2[j + 1], nums1[i])) / 2
                elif j + 1 < m:
                    return (nums2[j] + nums2[j + 1]) / 2
                else:
                    return (nums2[j] + nums1[i]) / 2


    def search(self, num, nums, l, r):
        """Search position in a sorted array.

        >>> Solution().search(3, [2], 0, 1)
        1
        >>> Solution().search(-1, [1, 3], 0, 2)
        0
        >>> Solution().search(1, [1, 3], 0, 2)
        0
        >>> Solution().search(3, [1, 3], 0, 2)
        1
        >>> Solution().search(2, [1, 3], 0, 2)
        1
        >>> Solution().search(4, [1, 3], 0, 2)
        2
        >>> Solution().search(-1, [1, 3, 5], 0, 3)
        0
        >>> Solution().search(1, [1, 3, 5], 0, 3)
        0
        >>> Solution().search(2, [1, 3, 5], 0, 3)
        1
        >>> Solution().search(3, [1, 3, 5], 0, 3)
        1
        >>> Solution().search(4, [1, 3, 5], 0, 3)
        2
        >>> Solution().search(5, [1, 3, 5], 0, 3)
        2
        >>> Solution().search(6, [1, 3, 5], 0, 3)
        3

        """
        if l >= r - 1:
            return l if num <= nums[l] else r

        if (l == r - 2) and (nums[l] < num <= nums[l + 1]):
            return l + 1
        if (l == r - 2) and nums[l] >= num:
            return l
        if (l == r - 2) and  num > nums[l + 1]:
            return r

        mid = (l + r - 1) // 2

        if nums[mid] < num:
            return self.search(num, nums, mid, r)
        elif nums[mid] > num:
            return self.search(num, nums, l, mid + 1)
        else:
            return mid

