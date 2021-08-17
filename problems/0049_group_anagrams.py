"""
Solution of the medium problem - "Group Anagrams",
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group Anagrams.

        >>> Solution().groupAnagrams([
        ...     'eat', 'tea', 'tan', 'ate', 'nat', 'bat',
        ... ])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        >>> Solution().groupAnagrams([''])
        [['']]
        >>> Solution().groupAnagrams(['a'])
        [['a']]

        """
        anagrams = defaultdict(list)

        for s in strs:
            anagrams[tuple(sorted(s))].append(s)

        return list(anagrams.values())

