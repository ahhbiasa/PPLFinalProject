from command_interface import Command

class JoinProjectCommand(Command):
    def __init__(self, collaboration_service, user, project):
        self.service = collaboration_service
        self.user = user
        self.project = project

    def execute(self):
        self.service.join_project(self.user, self.project)

    def undo(self):
        self.service.cancel_join_project(self.user, self.project)
