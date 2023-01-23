"""
Solution of the medium problem
https://leetcode.com/problems/snakes-and-ladders/
"Snakes and Ladders"
"""
from collections import deque
from itertools import chain
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """Return the least number of moves to reach the square `n^2`.

        >>> Solution().snakesAndLadders([
        ...     [-1, -1, -1, -1, -1, -1],
        ...     [-1, -1, -1, -1, -1, -1],
        ...     [-1, -1, -1, -1, -1, -1],
        ...     [-1, 35, -1, -1, 13, -1],
        ...     [-1, -1, -1, -1, -1, -1],
        ...     [-1, 15, -1, -1, -1, -1],
        ... ])
        4
        >>> Solution().snakesAndLadders([[-1, -1], [-1, 3]])
        1

        """
        board.reverse()
        for i in range(1, len(board), 2):
            board[i].reverse()
        arr = [None] + list(chain(*board))

        n = len(arr) - 1
        queue = deque([1])
        seen = {1}
        moves = 0

        while queue:
            for _ in range(len(queue)):
                square = queue.popleft()
                if square == n:
                    return moves

                for i in range(square + 1, min(square + 7, n + 1)):
                    nxt = arr[i] if arr[i] + 1 else i
                    if nxt in seen:
                        continue

                    queue.append(nxt)
                    seen.add(nxt)

            moves += 1                    

        return -1

