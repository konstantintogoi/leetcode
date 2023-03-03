"""
Solution of the easy problem
https://leetcode.com/problems/n-th-tribonacci-number/
"N-th Tribonacci Number"
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        """Given `n`, return the value of `T_n`.

        >>> Solution().tribonacci(4)
        4
        >>> Solution().tribonacci(25)
        1389537
        >>> Solution().tribonacci(0)
        0

        """
        nums = [0] * max(n + 1, 3)
        nums[1] = nums[2] = 1

        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]

        return nums[n]

