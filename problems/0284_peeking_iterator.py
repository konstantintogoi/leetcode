"""
Solution of the medium problem
https://leetcode.com/problems/peeking-iterator/
"Peeking Iterator"
"""
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None

    def peek(self):
        if self.peeked:
            return self.peeked

        self.peeked = self.iterator.next()
        return self.peeked

    def next(self):
        if self.peeked is not None:
            peeked = self.peeked
            self.peeked = None
            return peeked

        return self.iterator.next()

    def hasNext(self):
        return self.peeked is not None or self.iterator.hasNext()

