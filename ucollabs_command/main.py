from collaboration_service import CollaborationService
from controller import CollaborationController
from join_project_command import JoinProjectCommand

if __name__ == "__main__":
    # Shared project service
    service = CollaborationService()

    # Each user has their own command history (undo capability)
    controller_abhyasa = CollaborationController()
    controller_callista = CollaborationController()
    controller_reza = CollaborationController()

    # Create commands
    cmd_abhyasa = JoinProjectCommand(service, "Abhyasa", "Text Mining Project")
    cmd_callista = JoinProjectCommand(service, "Callista", "Text Mining Project")
    cmd_reza = JoinProjectCommand(service, "Reza", "Text Mining Project")

    # All users submit a join
    controller_abhyasa.submit(cmd_abhyasa)
    controller_callista.submit(cmd_callista)
    controller_reza.submit(cmd_reza)

    # Abhyasa undoes
    controller_abhyasa.undo_last()

    # Callista undoes
    controller_callista.undo_last()

    # Reza does nothing (his join remains)
