"""
Solution of the easy problem
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"Find Smallest Letter Greater Than Target"
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """Next Greatest Letter.

        >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'a')
        'c'
        >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'c')
        'f'
        >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'd')
        'f'
        >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'g')
        'j'
        >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'j')
        'c'
        >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'k')
        'c'

        """
        l, r = -1, len(letters)
        while l + 1 != r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid
            else:
                r = mid
        return letters[r] if r < len(letters) else letters[0]
