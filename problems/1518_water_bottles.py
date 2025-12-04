"""
Solution of the easy problem
https://leetcode.com/problems/water-bottles/
"Water Bottles"
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """Return the maximum number of water bottles you can drink.

        >>> Solution().numWaterBottles(9, 3)
        13
        >>> Solution().numWaterBottles(15, 4)
        19
        >>> Solution().numWaterBottles(25, 7)
        29

        """
        drunk = 0
        residue = 0
        while numBottles > 0:
            drunk += numBottles
            numBottles += residue
            residue = numBottles % numExchange
            numBottles = numBottles // numExchange

        return drunk

