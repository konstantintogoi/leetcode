"""
Solution of the medium problem - "Design Circular Queue",
https://leetcode.com/problems/design-circular-queue/
"""
class MyCircularQueue:
    """Circular Queue.

    >>> mcq = MyCircularQueue(3)
    >>> mcq.enQueue(1)
    True
    >>> mcq.enQueue(2)
    True
    >>> mcq.enQueue(3)
    True
    >>> mcq.enQueue(4)
    False
    >>> mcq.Rear()
    3
    >>> mcq.isFull()
    True
    >>> mcq.deQueue()
    True
    >>> mcq.enQueue(4)
    True
    >>> mcq.Rear()
    4

    >>> mcq = MyCircularQueue(6)
    >>> mcq.enQueue(6)
    True
    >>> mcq.Rear()
    6
    >>> mcq.Rear()
    6
    >>> mcq.deQueue()
    True
    >>> mcq.enQueue(5)
    True
    >>> mcq.Rear()
    5
    >>> mcq.deQueue()
    True
    >>> mcq.Front()
    -1
    >>> mcq.deQueue()
    False
    >>> mcq.deQueue()
    False
    >>> mcq.deQueue()
    False

    >>> mcq = MyCircularQueue(8)
    >>> mcq.enQueue(3)
    True
    >>> mcq.enQueue(9)
    True
    >>> mcq.enQueue(5)
    True
    >>> mcq.enQueue(0)
    True
    >>> mcq.deQueue()
    True
    >>> mcq.deQueue()
    True
    >>> mcq.isEmpty()
    False
    >>> mcq.isEmpty()
    False
    >>> mcq.Rear()
    0
    >>> mcq.Rear()
    0
    >>> mcq.deQueue()
    True

    >>> mcq = MyCircularQueue(2)
    >>> mcq.enQueue(1)
    True
    >>> mcq.enQueue(2)
    True
    >>> mcq.deQueue()
    True
    >>> mcq.enQueue(3)
    True
    >>> mcq.deQueue()
    True
    >>> mcq.enQueue(3)
    True
    >>> mcq.deQueue()
    True
    >>> mcq.enQueue(3)
    True
    >>> mcq.deQueue()
    True
    >>> mcq.Front()
    3

    """

    def __init__(self, k: int):
        self.k = k
        self.n = 0
        self.i = 0
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.i] = value
            self.n += 1
            self.i = (self.i + 1) % self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.isFull():
            self.q[self.i] = None
            self.n -= 1
            return True
        else:
            i = (self.i - self.n + self.k) % self.k
            self.q[i] = None
            self.n -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        elif self.isFull():
            return self.q[self.i]
        else:
            i = (self.i - self.n + self.k) % self.k
            return self.q[i]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            i = (self.i - 1 + self.k) % self.k
            return self.q[i]

    def isEmpty(self) -> bool:
        return self.n <= 0

    def isFull(self) -> bool:
        return self.n >= self.k

