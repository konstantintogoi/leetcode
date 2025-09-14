"""
Solution of the hard problem
https://leetcode.com/problems/permutation-sequence/
"Permutation Sequence"
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """Return the `k-th` permutation sequence.

        >>> Solution().getPermutation(3, 3)
        '213'
        >>> Solution().getPermutation(4, 9)
        '2314'
        >>> Solution().getPermutation(3, 1)
        '123'

        """
        skipped = 0
        digits = []

        nperms = 1
        for i in range(n, 0, -1):
            nperms *= i

        for i in range(1, n + 1):
            nperms /= (n - i + 1)

            for j in range(1, n + 1):
                if str(j) in digits:
                    continue

                if skipped <= k <= skipped + nperms:
                    digits.append(str(j))
                    break

                skipped += nperms

        return ''.join(digits)

