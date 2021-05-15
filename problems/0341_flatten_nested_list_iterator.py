"""
Solution of the medium problem - "Flatten Nested List Iterator",
https://leetcode.com/problems/flatten-nested-list-iterator/
"""
from typing import List


class NestedInteger:
    def __init__(self, int_or_list):
        self._integer = int_or_list if isinstance(int_or_list, int) else None
        self._list = int_or_list if self._integer is None else None

    def __repr__(self) -> str:
        """String representation."""
        return str(self._integer) if self._integer else str(self._list)

    def isInteger(self) -> bool:
        """Returns True if this NestedInteger holds a single integer."""
        return self._integer is not None

    def getInteger(self) -> int:
        """Returns the single integer or None."""
        return self._integer

    def getList(self) -> List['NestedInteger']:
        """Return the nested list or None."""
        return self._list


class NestedIterator:
    """Nested Iterator.

    >>> nested = [
    ...     NestedInteger([NestedInteger(1), NestedInteger(1)]),
    ...     NestedInteger(2),
    ...     NestedInteger([NestedInteger(1), NestedInteger(1)]),
    ... ]
    >>> res = []
    >>> it = NestedIterator(nested)
    >>> while it.hasNext():
    ...     res.append(it.next())
    >>> res
    [1, 1, 2, 1, 1]
    >>> 
    >>> nested = [
    ...     NestedInteger(1),
    ...     NestedInteger([
    ...         NestedInteger(4),
    ...         NestedInteger([
    ...             NestedInteger(6),
    ...         ]),
    ...     ])
    ... ]
    >>> res = []
    >>> it = NestedIterator(nested)
    >>> while it.hasNext():
    ...     res.append(it.next())
    >>> res
    [1, 4, 6]

    """

    def __init__(self, nestedList: List[NestedInteger]):
        self.items = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.items.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self) -> int:
        return self.items.pop(0)

    def hasNext(self) -> bool:
        return bool(self.items)

