"""
Solution of the medium problem
https://leetcode.com/problems/lru-cache/
"LRU Cache"
"""
from datetime import datetime
from heapq import heappop, heappush


class LRUCache:
    """Data structure that follows the constraints of a LRU Cache.

    >>> cache = LRUCache(2)
    >>> cache.put(1, 1)
    >>> cache.put(2, 2)
    >>> cache.get(1)
    1
    >>> cache.put(3, 3)
    >>> cache.get(2)
    -1
    >>> cache.put(4, 4)
    >>> cache.get(1)
    -1
    >>> cache.get(3)
    3
    >>> cache.get(4)
    4

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        value = self.values.pop(key)
        self.values[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.pop(key)
            self.values[key] = value
        elif len(self.values) == self.capacity:
            nextkey = next(iter(self.values))
            self.values.pop(nextkey)
            self.values[key] = value
        else:
            self.values[key] = value

