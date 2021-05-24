"""
Solution of the medium problem -
"Longest Substring Without Repeating Characters",
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Longest Substring.

        >>> Solution().lengthOfLongestSubstring('abcabcbb')
        3
        >>> Solution().lengthOfLongestSubstring('bbbbb')
        1
        >>> Solution().lengthOfLongestSubstring('pwwkew')
        3
        >>> Solution().lengthOfLongestSubstring('')
        0
        >>> Solution().lengthOfLongestSubstring('dvdf')
        3
        >>> Solution().lengthOfLongestSubstring('ohvhjdml')
        6

        """
        n = len(s)
        cursubs = ''
        maxsubs = ''
        for i in range(n):
            if s[i] in cursubs:
                cursubs = cursubs[cursubs.index(s[i]) + 1:] + s[i]
            else:
                cursubs += s[i]
            if len(cursubs) > len(maxsubs):
                maxsubs = cursubs
        return len(maxsubs)

