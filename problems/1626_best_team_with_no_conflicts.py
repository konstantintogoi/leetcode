"""
Solution of the medium problem
https://leetcode.com/problems/best-team-with-no-conflicts/
"Best Team With No Conflicts"
"""
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """Return the highest overall score of possible basketball teams.

        >>> Solution().bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5])
        34
        >>> Solution().bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1])
        16
        >>> Solution().bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1])
        6

        """
        dp = [0] * (1 + max(ages))  
        score_age = sorted(zip(scores, ages))

        for score, age in score_age:
            dp[age] = score + max(dp[:age + 1])

        return max(dp)

