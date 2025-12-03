"""
Solution of the medium problem
https://leetcode.com/problems/avoid-flood-in-the-city/
"Avoid Flood in The City"
"""
from collections import deque
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """Return an array `ans` where:

        - `ans.length` == `rains.length`,
        - `ans[i] == -1` if `rains[i] > 0`,
        - `ans[i] is the lake you choose to dry in the `ith` day

        >>> Solution().avoidFlood([1, 2, 3, 4])
        [-1, -1, -1, -1]
        >>> Solution().avoidFlood([1, 2, 0, 0, 2, 1])
        [-1, -1, 2, 1, -1, -1]
        >>> Solution().avoidFlood([1, 2, 0, 1, 2])
        []
        >>> Solution().avoidFlood([69, 0, 0, 0, 69])
        [-1, 69, 1, 1, -1]
        >>> Solution().avoidFlood([0, 1, 1])
        []
        >>> Solution().avoidFlood([1, 0, 2, 0, 2, 1])
        [-1, 1, -1, 2, -1, -1]
        >>> Solution().avoidFlood([1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3])
        [-1, 1, -1, 2, -1, 3, -1, 2, 1, 1, -1, -1, -1]

        """
        ans = []
        full = {}
        dryings = deque()

        for i, rain in enumerate(rains):
            ans.append(-1)

            if rain > 0:
                if rain in full:
                    for j, idrying in enumerate(dryings):
                        if idrying > full[rain]:
                            ans[idrying] = rain
                            # below is fast removing,
                            # i.e. dryings.remove(idrying)
                            dryings.rotate(-j)
                            dryings.popleft()
                            dryings.rotate(j)
                            break
                    else:
                        return []
                    full[rain] = i
                else:
                    full[rain] = i
            else:
                dryings.append(i)

        while dryings:
            ans[dryings.popleft()] = 1

        return ans

