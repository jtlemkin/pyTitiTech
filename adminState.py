from state import State
from button import Button

from psychopy import visual, event, gui

class AdminState(State):
    
    def __init__(self, app) -> None:
        self.app = app
        
        self.editConfigsButton = Button(app.win, pos=(0, 0.5), size=(1, 0.5), text="Edit configs")
        self.dataFileManagementButton = Button(app.win, pos=(-0.5,0), size=(1, 0.5), text="Data Management")
        self.subjectDataButton = Button(app.win, pos=(0.5, 0), size=(1, 0.5), text="Subject Data")
        self.exitButton = Button(app.win, pos=(0, -0.5), size=(1, 0.5), text="Exit", fillColor=(1,0,0))
        
        self.background = visual.Rect(app.win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def draw(self) -> None:
        self.background.draw()
        
        self.editConfigsButton.draw()
        self.dataFileManagementButton.draw()
        self.subjectDataButton.draw()
        self.exitButton.draw()
        
    def handle_input(self) -> None:
        if self.editConfigsButton.clicked_by(self.app.mouse):
            self.configureSettings()
            
        event.clearEvents()
    
    def configureSettings(self):
        constants = self.app.fileManager.read_constants()