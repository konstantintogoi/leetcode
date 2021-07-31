"""
Solution of the medium problem - "Parallel Courses",
https://leetcode.com/problems/parallel-courses/
"""
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """Minimum Semesters.

        >>> Solution().minimumSemesters(3, [[1, 3], [2, 3]])
        2
        >>> Solution().minimumSemesters(3, [[1, 2], [2, 3], [3, 1]])
        -1

        """
        graph = {i: [] for i in range(1, n + 1)}
        for a, b in relations:
            graph[a].append(b)

        visited = {}

        def dfs(node: int) -> int:
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1

            length = 1
            for n in graph[node]:
                l = dfs(n)
                if l == -1: return -1
                length = max(l + 1, length)
            visited[node] = length
            return length

        length = -1
        for node in graph.keys():
            l = dfs(node)
            if l == -1: return -1
            length = max(l, length)
        return length

