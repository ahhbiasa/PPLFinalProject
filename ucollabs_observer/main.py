from project_board import ProjectBoard
from user import User

# Create the subject
project_board = ProjectBoard()

# Create observers (users)
Abhyasa = User("Abhyasa")
Callista = User("Callista")
Reza = User("Reza")

# Subscriptions
project_board.subscribe(Abhyasa)
project_board.subscribe(Callista)

# Post a project
project_board.post_project("AI-Powered Study Group Finder")

# Charlie joins later
project_board.subscribe(Reza)

# Post another project
project_board.post_project("Web App for Peer Tutoring")