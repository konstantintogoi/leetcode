"""
Solution of the medium problem
https://leetcode.com/problems/design-a-food-rating-system/
"Design a Food Rating System"
"""
from collections import defaultdict
from typing import List


class FoodRatings:
    """Food rating system.

    >>> system = FoodRatings(
    ...     ['kimchi', 'miso', 'sushi', 'moussaka', 'ramen', 'bulgogi'],
    ...     ['korean', 'japanese', 'japanese', 'greek', 'japanese', 'korean'],
    ...     [9, 12, 8, 15, 14, 7],
    ... )
    >>> system.highestRated('korean')
    'kimchi'
    >>> system.highestRated('japanese')
    'ramen'
    >>> system.changeRating('sushi', 16)
    >>> system.highestRated('japanese')
    'sushi'
    >>> system.changeRating('ramen', 16)
    >>> system.highestRated('japanese')
    'ramen'

    """

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = defaultdict(lambda: defaultdict(set))
        self.top = defaultdict(lambda: [0, ''])
        self.foods = {}

        for i, food in enumerate(foods):
            self.foods[food] = [cuisines[i], ratings[i]]
            self.ratings[cuisines[i]][ratings[i]].add(food)
            if [-ratings[i], food] < self.top[cuisines[i]]:
                self.top[cuisines[i]] = [-ratings[i], food]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.foods[food]
        self.foods[food] = [cuisine, newRating]

        self.ratings[cuisine][newRating].add(food)
        if food in self.ratings[cuisine][oldRating]:
            self.ratings[cuisine][oldRating].remove(food)
        if not self.ratings[cuisine][oldRating]:
            del self.ratings[cuisine][oldRating]

        if [-newRating, food] < self.top[cuisine]:
            self.top[cuisine] = [-newRating, food]
        elif [-oldRating, food] == self.top[cuisine] and newRating > oldRating:
            self.top[cuisine] = [-newRating, food]
        elif [-oldRating, food] == self.top[cuisine] and newRating < oldRating:
            maxRating = max(self.ratings[cuisine].keys())
            maxRatedFoods = self.ratings[cuisine][maxRating]
            maxRatedFood = min(maxRatedFoods)
            self.top[cuisine] = [-maxRating, maxRatedFood]

    def highestRated(self, cuisine: str) -> str:
        return self.top[cuisine][1]

