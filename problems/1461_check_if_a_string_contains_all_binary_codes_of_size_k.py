"""
Solution of the medium problem
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
"Check if a String Contains All Binary Codes of Size K"
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """Has All Codes.

        >>> Solution().hasAllCodes('00110110', 2)
        True
        >>> Solution().hasAllCodes('00110', 2)
        True
        >>> Solution().hasAllCodes('0110', 1)
        True
        >>> Solution().hasAllCodes('0110', 2)
        False
        >>> Solution().hasAllCodes('0000000001011100', 4)
        False

        """
        return all((f'{{:0{k}b}}').format(i) in s for i in range(1 << k))
