from task import Task


class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.tasks = []
        self.counter_completed = 0

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)

            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.section_name}"

    def complete_task(self, task_name: str):
        for i in range(len(self.tasks)):
            if self.tasks[i] == task_name:
                self.tasks[i].completed = True
                return f"Completed task {task_name}"
            elif i == len(self.tasks):
                return f"Could not find task with the name {task_name}"

    def clean_section(self):
        for i in range(len(self.tasks)):
            if self.tasks[i].completed:
                self.tasks.remove(self.tasks[i])
                self.counter_completed += 1

        return_counter = self.counter_completed
        self.counter_completed = 0

        return f"Cleared {return_counter} tasks."

    def view_section(self):
        if not self.tasks:
            return f"Section {self.section_name}:\nNo tasks available."

        tasks_str_list = [task.details() for task in self.tasks]
        tasks_str = '\n'.join(tasks_str_list)

        return f"Section {self.section_name}:\n{tasks_str}"

