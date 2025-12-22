"""
Solution of the medium problem
https://leetcode.com/problems/design-task-manager/
"Design Task Manager"
"""
from collections import defaultdict
from heapq import heapify, heappush, heappop
from typing import List


class TaskManager:
    """A task management system that allows users to manage their tasks.

    >>> tm = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    >>> tm.add(4, 104, 5)
    >>> tm.edit(102, 8)
    >>> tm.execTop()
    3
    >>> tm.rmv(101)
    >>> tm.add(5, 105, 15)
    >>> tm.execTop()
    5

    """

    def __init__(self, tasks: List[List[int]]):
        self.tasks = []
        self.editedtasks = {}
        self.removedtasks = set()
        self.userIds = {}

        for userId, taskId, priority in tasks:
            self.tasks.append((-priority, -taskId, userId))
            self.userIds[taskId] = userId

        heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.tasks, (-priority, -taskId, userId))
        self.userIds[taskId] = userId

        if -taskId in self.removedtasks:
            del self.removedtasks[-taskId]
        if -taskId in self.editedtasks:
            del self.editedtasks[-taskId]

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.userIds[taskId]
        heappush(self.tasks, (-newPriority, -taskId, userId))
        self.editedtasks[-taskId, userId] = -newPriority

    def rmv(self, taskId: int) -> None:
        userId = self.userIds[taskId]
        self.removedtasks.add((-taskId, userId))

    def execTop(self) -> int:
        editedtask = None

        while self.tasks:
            priority, taskId, userId = heappop(self.tasks)

            if (taskId, userId) in self.removedtasks:
                continue

            if (taskId, userId) in self.editedtasks:
                newPriority = self.editedtasks[taskId, userId]
                editedtask = newPriority, taskId, userId
                if newPriority <= priority:
                    self.removedtasks.add((taskId, userId))
                    return userId
                continue

            if editedtask and editedtask < (priority, taskId, userId):
                heappush(self.tasks, (priority, taskId, userId))
                userId = editedtask[2]

            return userId

        if editedtask and editedtask[1] not in self.removedtasks:
            return editedtask[2]

        return -1

