class CollaborationService:
    def __init__(self):
        self.pending_requests = []

    def join_project(self, user, project):
        print(f"[JOIN] {user} has requested to join '{project}'")
        self.pending_requests.append((user, project))

    def cancel_join_project(self, user, project):
        if (user, project) in self.pending_requests:
            self.pending_requests.remove((user, project))
            print(f"[CANCEL] {user} has canceled their request to join '{project}'")
        else:
            print(f"[WARN] No pending join request for '{project}' by {user}")
