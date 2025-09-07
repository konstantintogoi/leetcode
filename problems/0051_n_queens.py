"""
Solution of the hard problem
https://leetcode.com/problems/n-queens/
"N-Queens"
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Return all distinct solutions to the n-queens puzzle.

        >>> Solution().solveNQueens(1)
        [['Q']]
        >>> Solution().solveNQueens(2)
        []
        >>> Solution().solveNQueens(3)
        []
        >>> Solution().solveNQueens(4)
        [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

        """
        board = [['.' for i in range(n + 2)] for j in range(n + 2)]
        self.boards = []
        self.placeQueens(board, n, n, 1)
        return self.boards

    def placeQueens(self, board, n, m, icurr):
        if m == 0:
            self.boards.append([
                ''.join(row[1:len(board)-1])
                for row in board[1:len(board)-1]
            ])
            return

        for i in range(icurr, len(board) - 1):
            for j in range(1, len(board) - 1):
                if self.isfree(board, i, j):
                    board[i][j] = 'Q'
                    self.placeQueens(board, n, m - 1, i)
                    board[i][j] = '.'

        return

    def isfree(self, board, i, j) -> bool:
        for k in range(1, len(board) - 1):
            if board[k][j] == 'Q':
                return False

        for l in range(1, len(board) - 1):
            if board[i][l] == 'Q':
                return False

        k, l = i, j
        while k < len(board) - 1 and l < len(board) - 1:
            if board[k][l] == 'Q':
                return False
            k += 1
            l += 1

        k, l = i, j
        while k > 0 and l > 0:
            if board[k][l] == 'Q':
                return False
            k -= 1
            l -= 1

        k, l = i, j
        while k > 0 and l < len(board) - 1:
            if board[k][l] == 'Q':
                return False
            k -= 1
            l += 1

        k, l = i, j
        while k < len(board) - 1 and l > 0:
            if board[k][l] == 'Q':
                return False
            k += 1
            l -= 1

        return True

