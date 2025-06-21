class CollaborationController:
    def __init__(self):
        self.history = []

    def submit(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("[INFO] No action to undo.")
