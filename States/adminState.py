from state import State
from button import Button

from psychopy import visual, event, gui

class AdminState(State):
    def on_load(self):
        super().on_load()
        
        self.editConfigsButton = Button(self.app.win, pos=(0, 0.5), size=(1, 0.5), text="Edit configs", on_click=self.configureSettings())
        self.dataFileManagementButton = Button(self.app.win, pos=(-0.5,0), size=(1, 0.5), text="Data Management", on_click=print)
        self.subjectDataButton = Button(self.app.win, pos=(0.5, 0), size=(1, 0.5), text="Subject Data", on_click=self.manageSubjects())
        self.exitButton = Button(self.app.win, pos=(0, -0.5), size=(1, 0.5), text="Exit", fillColor=(1,0,0), on_click=self.app.transition_to("subject"))
        
        self.subviews = [self.editConfigsButton, self.dataFileManagementButton, self.subjectDataButton, self.exitButton]
        
    def handle_input(self) -> None:
        if self.editConfigsButton.clicked_by(self.app.mouse):
            self.configureSettings()
        elif self.exitButton.clicked_by(self.app.mouse):
            self.app.transition_to("subject")
        elif self.subjectDataButton.clicked_by(self.app.mouse):
            subject = self.selectSubject()
            self.updateSubject(self.selectSubject())
    
    def configureSettings(self):
        constants = self.app.fileManager.read_constants()
        
        configGui = gui.DlgFromDict(constants, sortKeys = False)
        
        if configGui.OK:
            self.app.fileManager.write_constants(constants)
            
    def manageSubject(self):
        subject = self.selectSubject()
        self.updateSubject(self.selectSubject())    
            
    def selectSubject():
        subjects = {
            "Subjects" : []
        }