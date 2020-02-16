from States.deprecatedStartState import StartPsyViewController
from States.sessionState import SessionPsyViewController
from States.adminState import AdminPsyViewController
from States.shrinkingGoNoGoState import ShrinkingGoNoGoPsyViewController
from States.googleDriveState import GoogleDrivePsyViewController

from Framework.fileManager import FileManager

from psychopy import visual, event

class App:
    """
    This class manages the different states that our application can be in
    e.g. Transition between start state to trial state
    """
    
    state = None
    win = visual.Window(winType='pyglet')
    mouse = event.Mouse(win)
    
    fileManager = FileManager(subject_file = "Configuration/subject-data.csv",
                              constants_file = "Configuration/user-defined-constants.csv")

    def __init__(self, state) -> None:
        self.transition_to(state)
        
    def transition_to(self, state_name):
        print("transitioning to", state_name)
        
        inits = {
            "start" : StartPsyViewController,
            "admin" : AdminPsyViewController,
            "session" : SessionPsyViewController,
            "go_signal" : ShrinkingGoNoGoPsyViewController,
            "google_drive" : GoogleDrivePsyViewController,
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
        
app = App("start")
app.run()