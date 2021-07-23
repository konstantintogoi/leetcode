"""
Solution of the medium problem - "Keys and Rooms",
https://leetcode.com/problems/keys-and-rooms/
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """Can Visit All Rooms.

        >>> Solution().canVisitAllRooms([[1], [2], [3], []])
        True
        >>> Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
        False
        >>> Solution().canVisitAllRooms([[1], [2], [], [3]])
        False

        """
        colors = {}

        def dfs(i):
            if i in colors: return
            colors[i] = 'gray'
            for j in rooms[i]: dfs(j)
            colors[i] = 'black'

        dfs(0)
        return len(colors) == len(rooms)

