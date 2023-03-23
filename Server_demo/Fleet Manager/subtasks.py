"""
This file contains the functions that create sub-tasks from the main task.
"""

from enum import Enum
from typing import Dict, Union

class SubtaskType(Enum):
    MOVE_STRAIGHT = "move_straight"
    MOVE_LEFT = "move_left"
    MOVE_RIGHT = "move_right"
    MOVE_BACKWARD = "move_backward"
    STORE_PALLET = "store_pallet"
    RETRIEVE_PALLET = "retrieve_pallet"

class Subtask:
    def __init__(self, task_type: SubtaskType, data: Dict[str, Union[int, str]]) -> None:
        self.task_type = task_type
        self.data = data

    def __repr__(self) -> str:
        return f"{self.task_type.value}: {self.data}"