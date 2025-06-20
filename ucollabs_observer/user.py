class User:
    def __init__(self, name):
        self.name = name

    def update(self, project_title):
        print(f"🔔 {self.name} received notification: New project available - '{project_title}'")