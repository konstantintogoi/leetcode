"""
Solution of the medium problem
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
"Lexicographically Smallest Equivalent String"
"""
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """Return the lexicographically smallest equivalent string.

        >>> Solution().smallestEquivalentString('parker', 'morris', 'parser')
        'makkek'
        >>> Solution().smallestEquivalentString('hello', 'world', 'hold')
        'hdld'
        >>> Solution().smallestEquivalentString('leetcode', 'programs', 'sourcecode')
        'aauaaaaada'

        """
        djs = {}  # disjoint-set

        def find(x):
            djs.setdefault(x, x)
            if djs[x] != x:
                djs[x] = find(djs[x])
            return djs[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)

            if xroot > yroot:
                djs[xroot] = yroot
            else:
                djs[yroot] = xroot

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []
        for c in baseStr:
            res.append(find(c))

        return ''.join(res)

