from .task import Task
import json

TASK_FILE = "tasks.json"


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump([task.response() for task in tasks], file, indent=4)


def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            task_dict = json.load(file)
            return [Task.task_obj_from_dict(task) for task in task_dict]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
