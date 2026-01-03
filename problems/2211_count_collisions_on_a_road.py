"""
Solution of the medium problem
https://leetcode.com/problems/count-collisions-on-a-road/
"Count Collisions on a Road"
"""
class Solution:
    def countCollisions(self, directions: str) -> int:
        """Return the total number of collisions that will happen on the road.

        >>> Solution().countCollisions('RLRSLL')
        5
        >>> Solution().countCollisions('LLRR')
        0

        """
        dirs = directions.lstrip('L').rstrip('R')

        ncollisions = 0
        mstack = []

        for d in dirs:
            if d == 'R' and mstack and mstack[-1] == 'S':
                mstack = ['R']
                continue
            if d == 'R':
                mstack.append(d)
                continue
            if d == 'S' and mstack and mstack[-1] == 'S':
                continue
            if d == 'S' and mstack:
                ncollisions += len(mstack)
                mstack = ['S']
                continue
            if d == 'S':
                mstack.append(d)
                continue
            if d == 'L' and mstack and mstack[-1] == 'S':
                ncollisions += 1
                continue
            if d == 'L' and mstack:
                ncollisions += len(mstack) + 1
                mstack = ['S']
                continue

        return ncollisions

