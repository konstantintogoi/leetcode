"""
Solution of the medium problem
https://leetcode.com/problems/word-search/
"Word Search"
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Return `True` if `word` exists in the `board`.

        >>> Solution().exist([
        ...     ['A', 'B', 'C', 'E'],
        ...     ['S', 'F', 'C', 'S'],
        ...     ['A', 'D', 'E', 'E'],
        ... ], 'ABCCED')
        True
        >>> Solution().exist([
        ...     ['A', 'B', 'C', 'E'],
        ...     ['S', 'F', 'C', 'S'],
        ...     ['A', 'D', 'E', 'E'],
        ... ], 'SEE')
        True
        >>> Solution().exist([
        ...     ['A', 'B', 'C', 'E'],
        ...     ['S', 'F', 'C', 'S'],
        ...     ['A', 'D', 'E', 'E'],
        ... ], 'ABCB')
        False

        """
        m, n = len(board), len(board[0])

        def check(r, c, used, k) -> bool:
            if k == len(word):
                return True

            for i, j in {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}:
                if i < 0 or i == m: continue
                if j < 0 or j == n: continue
                if (i, j) in used: continue

                if word[k] == board[i][j]:
                    used.add((i, j))
                    if check(i, j, used, k + 1):
                        return True
                    used.discard((i, j))

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and check(i, j, {(i, j)}, 1):
                    return True

        return False

