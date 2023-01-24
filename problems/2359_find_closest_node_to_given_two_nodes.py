"""
Solution of the medium problem
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
"Find Closest Node to Given Two Nodes"
"""
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """Return the closest node to given two nodes.

        >>> Solution().closestMeetingNode([2, 2, 3, -1], 0, 1)
        2
        >>> Solution().closestMeetingNode([1, 2, -1], 0, 2)
        2

        """
        n = len(edges)

        def dfs(u, dst, dsts=None):
            dsts = dsts or {}
            dsts[u] = dst

            v = edges[u]
            if v > -1 and v not in dsts:
                dsts = dfs(v, dst + 1, dsts)

            return dsts

        dsts1 = dfs(node1, 0)
        dsts2 = dfs(node2, 0)

        dsts1 = {u: dsts1[u] for u in range(n) if u in dsts1 and u in dsts2}
        dsts2 = {u: dsts2[u] for u in range(n) if u in dsts1 and u in dsts1}

        if not dsts1 and not dsts2:
            return -1

        umin = -1
        mindst = float('inf')
        for u in range(n):
            if u in dsts1 and u in dsts2:
                dst = max(dsts1[u], dsts2[u])
                if dst < mindst:
                    mindst = dst
                    umin = u

        return umin

