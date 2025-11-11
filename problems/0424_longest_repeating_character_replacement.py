"""
Solution of the medium problem
https://leetcode.com/problems/longest-repeating-character-replacement/
"Longest Repeating Character Replacement"
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Return the longest substring's length containing the same letter.

        >>> Solution().characterReplacement('ABAB', 2)
        4
        >>> Solution().characterReplacement('AABABBA', 1)
        4
        >>> Solution().characterReplacement('ABCDE', 1)
        2
        >>> Solution().characterReplacement('ABAB', 0)
        1

        """
        i = 0
        j = 0
        chars = defaultdict(int)

        ans = 0
        while j < len(s):
            chars[s[j]] += 1
            countsum = sum(chars.values())
            maxcount = max(chars.values())

            while countsum - maxcount > k:
                chars[s[i]] -= 1
                if chars[s[i]] == 0:
                    del chars[s[i]]
                countsum = sum(chars.values())
                maxcount = max(chars.values())
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans

