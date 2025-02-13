import datetime


class Task:
    def __init__(
        self, task_name, is_complete=False, task_description="", createdAt=None
    ):
        self.task_name = task_name
        self.is_complete = is_complete
        self.task_description = task_description
        self.createdAt = datetime.datetime.now()

    def completed(self):
        """
        marks task as completed
        returns:
            Boolean True
        """
        self.is_complete = True

    def incomplete(self):
        """
        marks task as not completed
        returns:
            Boolean False
        """
        self.is_complete = False

    def response(self):

        return {
            "task_name": self.task_name,
            "task_description": self.task_description,
            "createdAt": self.createdAt.strftime("%d-%m-%Y %H:%M"),
            "is_complete": self.is_complete,
        }

    @staticmethod
    def task_obj_from_dict(task_dict):
        return Task(
            task_name=task_dict["task_name"],
            task_description=task_dict["task_description"],
            is_complete=task_dict["is_complete"],
            createdAt=task_dict["createdAt"],
        )
