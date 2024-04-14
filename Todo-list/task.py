class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Pending'}"
