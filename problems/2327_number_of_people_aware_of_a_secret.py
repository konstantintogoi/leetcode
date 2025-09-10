"""
Solution of the medium problem
https://leetcode.com/problems/number-of-people-aware-of-a-secret/
"Number of People Aware of a Secret"
"""
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """Return the number of people who know the secret.

        >>> Solution().peopleAwareOfSecret(6, 2, 4)
        5
        >>> Solution().peopleAwareOfSecret(4, 1, 3)
        6
        >>> Solution().peopleAwareOfSecret(684, 18, 496)
        653668527

        """
        mod = 1000000007
        delayed = [0] * delay
        remained = [0] * forget
        remained[forget - 1] = 1
        delayed[delay - 1] = 1
        ngossips = 0

        for day in range(n - 1):
            ngossips = (ngossips - remained[0]) % mod
            for i in range(1, forget):
                remained[i - 1] = remained[i]

            ngossips = (ngossips + delayed[0]) % mod
            for i in range(1, delay):
                delayed[i - 1] = delayed[i]

            delayed[delay - 1] = ngossips
            remained[forget - 1] = ngossips

        return (ngossips + sum(delayed)) % mod

