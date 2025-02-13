from task_operations import add_task, remove_task, display_tasks
from task import Task


tasks = []
title = input("title: ")
description = input("description: ")


item = Task(title, task_description=description)

print(add_task(tasks, item))

display_tasks(tasks)
