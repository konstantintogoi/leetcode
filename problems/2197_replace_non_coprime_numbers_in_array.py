"""
Solution of the hard problem
https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
"Replace Non-Coprime Numbers in Array"
"""
from collections import defaultdict
from math import ceil
from typing import Dict, List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """Return the final modified array.

        >>> Solution().replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2])
        [12, 7, 6]
        >>> Solution().replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3])
        [2, 1, 1, 3]
        >>> Solution().replaceNonCoprimes(
        ...     [517, 11, 121, 517, 3, 51, 3, 1887, 5]
        ... )
        [5687, 1887, 5]
        >>> Solution().replaceNonCoprimes(
        ...     [287, 41, 49, 287, 899, 23, 23, 20677, 5, 825]
        ... )
        [2009, 20677, 825]

        """
        self.factcache = {}
        self.gcdcache = {}

        def gcd(a: int, b: int):
            if (a, b) in self.gcdcache:
                return self.gcdcache[a, b]
            if (b, a) in self.gcdcache:
                return self.gcdcache[b, a]

            afactors = self.factorize(a)
            bfactors = self.factorize(b)

            g = 1
            for prime in afactors.keys() & bfactors.keys():
                g *= prime ** (min(afactors[prime], bfactors[prime]))

            return g

        result = [nums[0]]

        for i in range(1, len(nums)):
            lastcoprime = result.pop()
            g = gcd(lastcoprime, num := nums[i])

            while g > 1:
                result.append(lastcoprime * num // g)

                if len(result) > 1:
                    num = result.pop()
                    lastcoprime = result.pop()
                    g = gcd(lastcoprime, num)
                else:
                    break
            else:
                result.append(lastcoprime)
                result.append(num)

        return result

    def factorize(self, n: int) -> Dict[int, int]:
        if n in self.factcache:
            return self.factcache[n]

        factorization = defaultdict(int)

        num = n
        while num % 2 == 0:
            factorization[2] += 1
            num /= 2

        i = 3
        while i <= num:
            while num % i == 0:
                factorization[i] += 1
                num /= i
            i += 2

        self.factcache[n] = factorization
        return factorization

