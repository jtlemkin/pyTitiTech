#exec(open('pyTitiTechnology.py').read())

from psychopy import visual, event
from States.subjectSelectionState import SubjectSelectionState
from States.sessionState import SessionState
from States.adminState import AdminState
from fileManager import FileManager

class App:
    """
    This class manages the different states that our application can be in
    e.g. Transition between start state to trial state
    """
    
    state = None
    win = visual.Window()
    mouse = event.Mouse(win)
    
    fileManager = FileManager(subject_file = "Constants/subject-data.csv", 
                              constants_file = "Constants/user-defined-constants.csv")

    def __init__(self, state) -> None:
        self.transition_to(state)
        
    def transition_to(self, state_name):
        print("transitioning to", state_name)
        
        inits = {
            "subject" : SubjectSelectionState,
            "admin" : AdminState,
            "session" : SessionState
        }
        
        newState = inits[state_name]()

        
        if self.state:
            self.state.prepare_for_transition_to(newState)
            
        self.state = newState
        self.state.app = self
        
        self.state.on_load()
        
    def run(self):
        while True:
            self.state.draw()
            self.win.flip()
            
            self.state.on_appear()
            self.state.handle_input()
            
            if event.getKeys() and event.getKeys()[0] == 'escape':
                break
            
            event.clearEvents()
        

starting_state_name = "subject"
app = App(starting_state_name)
app.run()