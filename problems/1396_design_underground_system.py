"""
Solution of "Design Underground System" problem at
https://leetcode.com/problems/design-underground-system/
"""
class UndergroundSystem:
    """Underground System.

    >>> s = UndergroundSystem()
    >>> s.checkIn(45, 'Leyton', 3)
    >>> s.checkIn(32, 'Paradise', 8)
    >>> s.checkIn(27, 'Leyton', 10)
    >>> s.checkOut(45, 'Waterloo', 15)
    >>> s.checkOut(27, 'Waterloo', 20)
    >>> s.checkOut(32, 'Cambridge', 22)
    >>> s.getAverageTime('Paradise', 'Cambridge')
    14
    >>> s.getAverageTime('Leyton', 'Waterloo')
    11.0
    >>> s.checkIn(10, 'Leyton', 24)
    >>> s.getAverageTime('Leyton', 'Waterloo')
    11.0
    >>> s.checkOut(10, 'Waterloo', 38)
    >>> s.getAverageTime('Leyton', 'Waterloo')
    12.0

    >>> s = UndergroundSystem()
    >>> s.checkIn(10, 'Leyton', 3)
    >>> s.checkOut(10, 'Paradise', 8)
    >>> s.getAverageTime('Leyton', 'Paradise')
    5
    >>> s.checkIn(5, 'Leyton', 10)
    >>> s.checkOut(5, 'Paradise', 16)
    >>> s.getAverageTime('Leyton', 'Paradise')
    5.5
    >>> s.checkIn(2, 'Leyton', 21)
    >>> s.checkOut(2, 'Paradise', 30)
    >>> s.getAverageTime('Leyton', 'Paradise')
    6.666666666666667

    """

    def __init__(self):
        self.table = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.table[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStationName, startT = self.table[id]
        if (startStationName, stationName) in self.averages:
            n, avg = self.averages[startStationName, stationName]
            self.averages[startStationName, stationName] = (
                n + 1, (n * avg + t - startT) / (n + 1)
            )
        else:
            self.averages[startStationName, stationName] = 1, t - startT
        self.table.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[startStation, endStation][1]

