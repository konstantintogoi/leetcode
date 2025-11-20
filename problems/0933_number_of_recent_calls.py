"""
Solution of the easy problem
https://leetcode.com/problems/number-of-recent-calls/
"Number of Recent Calls"
"""
class RecentCounter:
    """Counts the number of recent requests within a certain time frame.

    >>> counter = RecentCounter()
    >>> counter.ping(1)
    1
    >>> counter.ping(100)
    2
    >>> counter.ping(3001)
    3
    >>> counter.ping(3002)
    3

    """

    def __init__(self):
        self.requests = {}

    def ping(self, t: int) -> int:
        prevt = next(iter(self.requests), t)

        while self.requests and t - prevt > 3000:
            self.requests.pop(prevt)
            prevt = next(iter(self.requests), prevt)

        self.requests[t] = True
        return len(self.requests)

