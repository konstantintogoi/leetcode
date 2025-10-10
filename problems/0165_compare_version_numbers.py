"""
Solution of the medium problem
https://leetcode.com/problems/compare-version-numbers/
"Compare Version Numbers"
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """Compare `version1` and `version2` return -1 or 1 or 0.

        >>> Solution().compareVersion('1.2', '1.10')
        -1
        >>> Solution().compareVersion('1.01', '1.001')
        0
        >>> Solution().compareVersion('1.0', '1.0.0.0')
        0
        >>> Solution().compareVersion('7.5.2.4', '7.5.3')
        -1

        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        vlen = max(len(v1), len(v2))

        v1.extend(['0'] * (vlen - len(v1)))
        v2.extend(['0'] * (vlen - len(v2)))

        for i in range(vlen):
            r1 = int(v1[i])
            r2 = int(v2[i])

            if r1 > r2:
                return 1
            elif r1 < r2:
                return -1

        return 0

