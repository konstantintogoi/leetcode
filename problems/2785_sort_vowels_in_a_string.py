"""
Solution of the medium problem
https://leetcode.com/problems/sort-vowels-in-a-string/
"Sort Vowels in a String"
"""
class Solution:
    def sortVowels(self, s: str) -> str:
        """Return a string with sorted vowels.

        >>> Solution().sortVowels('lEetcOde')
        'lEOtcede'
        >>> Solution().sortVowels('lYmpH')
        'lYmpH'

        """
        vowels = dict.fromkeys([
            'A', 'E', 'I', 'O', 'U',
            'a', 'e', 'i', 'o', 'u',
        ], 0)

        ixs = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowels[s[i]] += 1
                ixs.append(i)

        i = 0
        a = list(s)
        for c in vowels:
            while vowels[c]:
                vowels[c] -= 1
                a[ixs[i]] = c
                i += 1

        return ''.join(a)

