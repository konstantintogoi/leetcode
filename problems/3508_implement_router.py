"""
Solution of the medium problem
https://leetcode.com/problems/implement-router/
"Implement Router"
"""
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Router:
    """A data structure that can efficiently manage data packets.

    >>> rt = Router(3)
    >>> rt.addPacket(1, 4, 90)
    True
    >>> rt.addPacket(2, 5, 90)
    True
    >>> rt.addPacket(1, 4, 90)
    False
    >>> rt.addPacket(3, 5, 95)
    True
    >>> rt.addPacket(4, 5, 105)
    True
    >>> rt.forwardPacket()
    [2, 5, 90]
    >>> rt.addPacket(5, 2, 110)
    True
    >>> rt.getCount(5, 100, 110)
    1
    >>> rt = Router(2)
    >>> rt.addPacket(7, 4, 90)
    True
    >>> rt.forwardPacket()
    [7, 4, 90]
    >>> rt.forwardPacket()
    []

    """

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit

        self.packets = {}
        self.psums = defaultdict(int)
        self.nsums = defaultdict(int)

        self.addts = defaultdict(lambda: [0, 1000000001])
        self.delts = defaultdict(lambda: [0, 1000000001])
        self.lastAddTimestamp = {}  # destination -> last added timestamp
        self.lastDelTimestamp = {}  # destination -> last dl/fw timestamp

    def increasePrefixSum(self, destination: int, timestamp: int) -> None:
        if destination not in self.lastAddTimestamp:
            self.psums[destination, 0] = 0
            self.psums[destination, timestamp] += 1
            self.psums[destination, 1000000001] += 1
            self.lastAddTimestamp[destination] = timestamp
        elif self.lastAddTimestamp[destination] == timestamp:
            self.psums[destination, timestamp] += 1
            self.psums[destination, 1000000001] += 1
            self.lastAddTimestamp[destination] = timestamp
        else:
            self.psums[destination, 1000000001] += 1
            lasttimestamp = self.lastAddTimestamp[destination]
            self.psums[destination, timestamp - 1] = self.psums[destination, lasttimestamp]
            self.psums[destination, timestamp] = self.psums[destination, lasttimestamp] + 1
            self.lastAddTimestamp[destination] = timestamp
            self.addts[destination][-1] = timestamp - 1
            self.addts[destination].append(1000000001)

    def decreasePrefixSum(self, destination: int, timestamp: int) -> None:
        if destination not in self.lastDelTimestamp:
            self.nsums[destination, 0] = 0
            self.nsums[destination, timestamp] += 1
            self.nsums[destination, 1000000001] += 1
            self.lastDelTimestamp[destination] = timestamp
        elif self.lastDelTimestamp[destination] == timestamp:
            self.nsums[destination, timestamp] += 1
            self.nsums[destination, 1000000001] += 1
            self.lastDelTimestamp[destination] = timestamp
        else:
            self.nsums[destination, 1000000001] += 1
            lasttimestamp = self.lastDelTimestamp[destination]
            self.nsums[destination, timestamp - 1] = self.psums[destination, lasttimestamp]
            self.nsums[destination, timestamp] = self.nsums[destination, lasttimestamp] + 1
            self.lastDelTimestamp[destination] = timestamp
            self.delts[destination][-1] = timestamp - 1
            self.delts[destination].append(1000000001)

    def appendAddTimestamp(self, dst: int, ts: int) -> None:
        if len(self.addts[dst]) == 2 or ts != self.addts[dst][-2]:
            self.addts[dst][-1] = ts
            self.addts[dst].append(1000000001)

    def appendDelTimestamp(self, dst: int, ts: int) -> None:
        if len(self.delts[dst]) == 2 or ts != self.delts[dst][-2]:
            self.delts[dst][-1] = ts
            self.delts[dst].append(1000000001)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packets:
            return False

        if len(self.packets) == self.memoryLimit:
            s, d, t = next(iter(self.packets))
            self.decreasePrefixSum(d, t)
            self.appendDelTimestamp(d, t)
            del self.packets[s, d, t]

        self.increasePrefixSum(destination, timestamp)
        self.packets[source, destination, timestamp] = None
        self.appendAddTimestamp(destination, timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if self.packets:
            s, d, t = next(iter(self.packets))
            self.decreasePrefixSum(d, t)
            self.appendDelTimestamp(d, t)
            del self.packets[s, d, t]

            return [s, d, t]

        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if len(ats := self.addts[destination]) == 2 or startTime > ats[-2] or endTime < ats[1]:
            return 0
        if (dts := self.delts[destination]) and endTime < dts[-2]:
            return 0

        st = ats[bisect_left(ats, startTime) - 1]
        et = ats[bisect_left(ats, endTime)]
        nadd = self.psums[destination, et] - self.psums[destination, st]

        st = dts[bisect_left(dts, startTime) - 1]
        et = dts[bisect_left(dts, endTime)]
        ndel = self.nsums[destination, et] - self.nsums[destination, st]

        return nadd - ndel

