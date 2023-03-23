"""
This file contains the functions that check the availability of the robots and assign tasks to them.
"""

import heapq
from typing import List, Dict
from subtasks import Subtask, SubtaskType

class TaskAssignment:
    def __init__(self, robot_id: int, task: Dict[str, int]) -> None:
        self.robot_id = robot_id
        self.task = task

    def __lt__(self, other) -> bool:
        # This is used for the priority queue
        return self.task["priority"] < other.task["priority"]

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
        self.priority_queue = []

    def add_task(self, from_location: int, to_location: int, task_type: SubtaskType, priority: int) -> None:
        # Create a new task with the specified subtasks
        subtasks = [Subtask(task_type, {"from_location": from_location, "to_location": to_location})]
        self.tasks.append({"subtasks": subtasks, "priority": priority})

        # Add the task to the priority queue
        task_assignment = TaskAssignment(0, self.tasks[-1])
        heapq.heappush(self.priority_queue, task_assignment)

    def get_next_task(self) -> Dict[str, List[Subtask]]:
        # Get the highest priority task from the priority queue
        task_assignment = heapq.heappop(self.priority_queue)
        task = task_assignment.task

        # Divide the task into subtasks and return it
        subtasks = task["subtasks"]
        return {"subtasks": subtasks}