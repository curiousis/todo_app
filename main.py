from task_manager.task import Task
from task_manager.task_operations import add_task, remove_task, display_tasks
from task_manager.task_storage import save_tasks, load_tasks


def main():
    tasks = load_tasks()

    print("\nCurrent Tasks:")
    display_tasks(tasks)

    title = input("\ntitle: ").strip()
    description = input("description: ").strip()

    new_task = Task(title, task_description=description)

    print(add_task(tasks, new_task))
    save_tasks(tasks)

    print("\nUpdated Task List:")
    display_tasks(tasks)


if __name__ == "__main__":
    main()
