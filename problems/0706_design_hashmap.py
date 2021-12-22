"""
Solution of the easy problem
https://leetcode.com/problems/design-hashmap/
"Design Hashmap"
"""
class HashMap:
    """Hash Map.

    >>> hmap = HashMap()
    >>> hmap.put(1, 1)
    >>> hmap.put(2, 2)
    >>> hmap.get(1)
    1
    >>> hmap.get(3)
    -1
    >>> hmap.put(2, 1)
    >>> hmap.get(2)
    1
    >>> hmap.remove(2)
    >>> hmap.get(2)
    -1

    """

    def __init__(self):
        self.maxsize = 10000
        self.table = [None] * self.maxsize

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hkey = key % self.maxsize
        colkey = None
        for i, pair in enumerate(self.table[hkey] or ()):
            if pair and pair[0] == key:
                self.table[hkey][i] = (key, value)
                return
            if colkey is None and pair is None:
                colkey = i
                continue

        if self.table[hkey] is None:
            self.table[hkey] = [(key, value)]
        elif colkey is None:
            self.table[hkey].append((key, value))
        else:
            self.table[hkey][colkey] = (key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        hkey = key % self.maxsize
        for i, pair in enumerate(self.table[hkey] or ()):
            if pair and pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        """
        hkey = key % self.maxsize
        for i, pair in enumerate(self.table[hkey] or ()):
            if pair and pair[0] == key:
                self.table[hkey][i] = None
                return
