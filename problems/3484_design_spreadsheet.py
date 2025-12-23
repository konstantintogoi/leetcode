"""
Solution of the medium problem
https://leetcode.com/problems/design-spreadsheet/
"Design Spreadsheet"
"""
class Spreadsheet:
    """A grid with 26 columns (from `A` to `Z`) and a given number of `rows`.

    >>> ss = Spreadsheet(3)
    >>> ss.getValue('=5+7')
    12
    >>> ss.setCell('A1', 10)
    >>> ss.getValue('=A1+6')
    16
    >>> ss.setCell('B2', 15)
    >>> ss.getValue('=A1+B2')
    25
    >>> ss.resetCell('A1')
    >>> ss.getValue('=A1+B2')
    15

    """

    def __init__(self, rows: int):
        self.sheet = [[0 for i in range(26)] for j in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        i = int(cell[1:]) - 1
        j = ord(cell[0]) - 65
        self.sheet[i][j] = value

    def resetCell(self, cell: str) -> None:
        i = int(cell[1:]) - 1
        j = ord(cell[0]) - 65
        self.sheet[i][j] = 0

    def getCell(self, cell: str) -> int:
        i = int(cell[1:]) - 1
        j = ord(cell[0]) - 65
        return self.sheet[i][j]

    def getValue(self, formula: str) -> int:
        a, b = formula.replace('=', ' ').replace('+', ' ').split()
        a = self.getCell(a) if a[0].isalpha() else int(a)
        b = self.getCell(b) if b[0].isalpha() else int(b)
        return a + b

