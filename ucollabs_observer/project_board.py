class ProjectBoard:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, project_title):
        for observer in self._observers:
            observer.update(project_title)

    def post_project(self, project_title):
        print(f"\n📢 New project posted: {project_title}")
        self.notify(project_title)