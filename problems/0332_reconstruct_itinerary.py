"""
Solution of the hard problem
https://leetcode.com/problems/reconstruct-itinerary/
"Reconstruct Itinerary"
"""
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """Reconstruct the itinerary in order and return it.

        >>> Solution().findItinerary([
        ...     ['MUC', 'LHR'], ['JFK', 'MUC'],
        ...     ['SFO', 'SJC'], ['LHR', 'SFO'],
        ... ])
        ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
        >>> Solution().findItinerary([
        ...     ['JFK', 'SFO'], ['JFK', 'ATL'],
        ...     ['SFO', 'ATL'], ['ATL', 'JFK'],
        ...     ['ATL', 'SFO'],
        ... ])
        ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']

        """
        adjlists = defaultdict(list)

        for departure, arrival in sorted(tickets, reverse=True):
            adjlists[departure].append(arrival)

        itenerary = []
        def dfs(departure):
            while adjlists[departure]:
                dfs(adjlists[departure].pop())
            itenerary.append(departure)

        dfs('JFK')
        return itenerary[::-1]

