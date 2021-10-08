"""
Solution of the hard problem
https://leetcode.com/problems/sudoku-solver/
"Sudoku Solver"
"""
from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Solve Sudoku.

        >>> board = [
        ...     ["5","3",".",".","7",".",".",".","."],
        ...     ["6",".",".","1","9","5",".",".","."],
        ...     [".","9","8",".",".",".",".","6","."],
        ...     ["8",".",".",".","6",".",".",".","3"],
        ...     ["4",".",".","8",".","3",".",".","1"],
        ...     ["7",".",".",".","2",".",".",".","6"],
        ...     [".","6",".",".",".",".","2","8","."],
        ...     [".",".",".","4","1","9",".",".","5"],
        ...     [".",".",".",".","8",".",".","7","9"],
        ... ]
        >>> Solution().solveSudoku(board)
        >>> for row in board:
        ...     print(row)
        ['5', '3', '4', '6', '7', '8', '9', '1', '2']
        ['6', '7', '2', '1', '9', '5', '3', '4', '8']
        ['1', '9', '8', '3', '4', '2', '5', '6', '7']
        ['8', '5', '9', '7', '6', '1', '4', '2', '3']
        ['4', '2', '6', '8', '5', '3', '7', '9', '1']
        ['7', '1', '3', '9', '2', '4', '8', '5', '6']
        ['9', '6', '1', '5', '3', '7', '2', '8', '4']
        ['2', '8', '7', '4', '1', '9', '6', '3', '5']
        ['3', '4', '5', '2', '8', '6', '1', '7', '9']

        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        dots = []

        for i in range(9):
            for j in range(9):
                digit = board[i][j]

                if digit == '.':
                    dots.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxs[i // 3, j // 3].add(digit)

        def dfs():
            if not dots:
                return True

            i, j = dots.pop()

            for digit in '123456789':
                if digit in rows[i]:
                    continue
                elif digit in cols[j]:
                    continue
                elif digit in boxs[i // 3, j // 3]:
                    continue

                board[i][j] = digit
                rows[i].add(digit)
                cols[j].add(digit)
                boxs[i // 3, j // 3].add(digit)

                if dfs():
                    return True

                board[i][j] = '.'
                rows[i].remove(digit)
                cols[j].remove(digit)
                boxs[i // 3, j // 3].remove(digit)

            dots.append((i, j))

            return False

        dfs()
