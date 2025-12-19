"""
Solution of the medium problem
https://leetcode.com/problems/water-bottles-ii/
"Water Bottles II"
"""
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """Return the maximum number of water bottles you can drink.

        >>> Solution().maxBottlesDrunk(13, 6)
        15
        >>> Solution().maxBottlesDrunk(10, 3)
        13

        """
        drunk = 0
        residue = 0

        while numBottles > 0:
            drunk += numBottles
            residue = numBottles + residue
            numBottles = 0

            while residue >= numExchange:
                numBottles += 1
                residue -= numExchange
                numExchange += 1

        return drunk

