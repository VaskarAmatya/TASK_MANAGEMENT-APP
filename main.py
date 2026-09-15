import os
import json

class todo:
    def __init__(self, file_name="tasks.json"):
        self.filename = file_name
        self.tasks = self.load_tasks()


    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                json.load(f)
        return[]

    def view_task(self):
        if not self.tasks:
            print("NO TASKS")
            return