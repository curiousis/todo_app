def add_task(tasks, task):
    if any(t.task_name == task.task_name for t in tasks):
        return "task already exists"
    elif task.task_name.strip():
        tasks.append(task)
        return "task added"
    else:
        return "cannot add an empty task"


def remove_task(tasks, task):
    for item in tasks:
        if item.task_name == task:
            task.remove(task)
            return "task removed"
    return "task not found"


def display_tasks(tasks):
    if not tasks:
        print("No tasks available")
    for task in tasks:
        print(task.response())
