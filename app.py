#exec(open('pyTitiTechnology.py').read())

from psychopy import visual, event
from subjectSelectionState import SubjectSelectionState
from adminState import AdminState
from fileManager import FileManager

class App:
    """
    This class manages the different states that our application can be in
    e.g. Transition between start state to trial state
    """
    
    state = None
    win = visual.Window(size=(800,600))
    mouse = event.Mouse(win)
    
    fileManager = FileManager(subject_file = "subject-data.csv", 
                              constants_file = "user-defined-constants.csv")

    def __init__(self, state) -> None:
        self.transition_to(state)
        
    def transition_to(self, state):
        inits = {
            "subject" : SubjectSelectionState,
            "admin" : AdminState
        }
        
        self.state = inits[state](self)

app = App("subject")

while True:
    app.state.draw()
    app.state.handle_input()
    app.win.flip()