"""
Solution of the medium problem
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"Longest Subarray of 1's After Deleting One Element"
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """Return the size of the longest non-empty subarray.

        >>> Solution().longestSubarray([1, 1, 0, 1])
        3
        >>> Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])
        5
        >>> Solution().longestSubarray([1, 1, 1])
        2
        >>> Solution().longestSubarray([1, 0, 0, 0])
        1

        """
        seqlens = []

        seqlen = 0
        prevseqlen = 0
        haszero = False

        for num in nums:
            if num == 1:
                seqlen += 1
            elif seqlen:
                haszero = True
                seqlens.append((prevseqlen, seqlen))
                prevseqlen = seqlen
                seqlen = 0
            else:
                haszero = True
                prevseqlen = 0

        if seqlen:
            seqlens.append((prevseqlen, seqlen))
        if not seqlens:
            return 0
        if len(seqlens) == 1:
            return seqlens[0][0] + seqlens[0][1] - (not haszero)

        return max(prevseqlen + seqlen for prevseqlen, seqlen in seqlens)

