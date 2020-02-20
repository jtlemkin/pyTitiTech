from controllers.login_vc import LoginViewController

from psy_framework.fileManager import FileManager

from psychopy import visual, event


class App:
    """
    This class manages the different states that our application can be in
    e.g. Transition between start state to trial state
    """
    
    state = None
    win = visual.Window(winType='pyglet')
    mouse = event.Mouse(win)
    
    fileManager = FileManager(subject_file="config/subject-data.csv",
                              constants_file="config/user-defined-constants.csv")

    def __init__(self, state) -> None:
        self.transition_to(state)
        
    def transition_to(self, state_name):
        print("transitioning to", state_name)
        
        inits = {
            "login" : LoginViewController
        }
        
        new_state = inits[state_name]()
        
        if self.state:
            self.state.prepare_for_transition_to(new_state)
            
        self.state = new_state
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


app = App("login")
app.run()