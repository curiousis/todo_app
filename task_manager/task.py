import datetime


class Task:
    def __init__(self, task_name, is_complete=False, task_description=""):
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
        status = "completed" if self.is_complete else "Incomplete"

        return {
            "title": self.task_name,
            "status": status,
            "description": self.task_description,
            "createdAt": self.createdAt.strftime("%d-%m-%Y %H:%M"),
        }
