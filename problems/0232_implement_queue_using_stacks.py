"""
Solution of the easy problem
https://leetcode.com/problems/implement-queue-using-stacks/
"Implement Queue using Stacks"
"""
class MyQueue:
    """A first in first out (FIFO) queue with only two stacks.

    >>> queue = MyQueue()
    >>> queue.push(1)
    >>> queue.push(2)
    >>> queue.peek()
    1
    >>> queue.pop()
    1
    >>> queue.empty()
    False

    """

    def __init__(self):
        self.spush = []
        self.spop = []

    def push(self, x: int) -> None:
        self.spush.append(x)

    def pop(self) -> int:
        self.peek()
        return self.spop.pop()

    def peek(self) -> int:
        if not self.spop:
            while self.spush:
                self.spop.append(self.spush.pop())
        return self.spop[-1]

    def empty(self) -> bool:
        return not self.spush and not self.spop

