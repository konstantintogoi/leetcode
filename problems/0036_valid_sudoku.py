"""
Solution of the medium problem
https://leetcode.com/problems/valid-sudoku/
"Valid Sudoku"
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Is Valid Sudoku.

        >>> Solution().isValidSudoku([
        ...     ["5","3",".",".","7",".",".",".","."],
        ...     ["6",".",".","1","9","5",".",".","."],
        ...     [".","9","8",".",".",".",".","6","."],
        ...     ["8",".",".",".","6",".",".",".","3"],
        ...     ["4",".",".","8",".","3",".",".","1"],
        ...     ["7",".",".",".","2",".",".",".","6"],
        ...     [".","6",".",".",".",".","2","8","."],
        ...     [".",".",".","4","1","9",".",".","5"],
        ...     [".",".",".",".","8",".",".","7","9"],
        ... ])
        True
        >>> Solution().isValidSudoku([
        ...     ["8","3",".",".","7",".",".",".","."],
        ...     ["6",".",".","1","9","5",".",".","."],
        ...     [".","9","8",".",".",".",".","6","."],
        ...     ["8",".",".",".","6",".",".",".","3"],
        ...     ["4",".",".","8",".","3",".",".","1"],
        ...     ["7",".",".",".","2",".",".",".","6"],
        ...     [".","6",".",".",".",".","2","8","."],
        ...     [".",".",".","4","1","9",".",".","5"],
        ...     [".",".",".",".","8",".",".","7","9"],
        ... ])
        False

        """
        rows = [[set(), 0] for _ in range(9)]
        cols = [[set(), 0] for _ in range(9)]
        boxs = [[[set(), 0], [set(), 0], [set(), 0]] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                x = i // 3
                y = j // 3
                cell = board[i][j]

                if cell != '.':
                    rows[i][0].add(cell)
                    cols[j][0].add(cell)
                    boxs[x][y][0].add(cell)

                    rows[i][1] += 1
                    cols[j][1] += 1
                    boxs[x][y][1] += 1

        for cells, cnt in rows:
            if len(cells) != cnt:
                return False

        for cells, cnt in cols:
            if len(cells) != cnt:
                return False

        for i in range(3):
            for j in range(3):
                cells, cnt = boxs[i][j]
                if len(cells) != cnt:
                    return False

        return True
