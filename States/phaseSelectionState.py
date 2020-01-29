from state import State
from button import Button

from psychopy import visual, event, gui

class PhaseSelectionState(State):
    subject = None
    
    def on_load(self):
        super().on_load()
        
        self.goSignalButton = Button(self.app.win, pos=(0, 0.5), size=(1.5, 0.5), text="Go Signal", on_click=print)
        self.waitScreenButton = Button(self.app.win, pos=(0, 0.25), size=(1.5, 0.5), text="Wait Screen", on_click=print)
        self.alternatingStopSignalButton = Button(self.app.win, pos=(0, 0), size=(1.5, 0.5), text="Alternating Stop Signal", on_click=print)
        self.randomStopSignalButton = Button(self.app.win, pos=(0, -0.25), size=(1.5, 0.5), text="Random Stop Signal", on_click=print)
        self.experimentButton = Button(self.app.win, pos=(0, -0.5), size=(1.5, 0.5), text="Experiment", on_click=print)
        
        self.subviews = [self.goSignalButton, self.waitScreenButton, self.alternatingStopSignalButton, self.randomStopSignalButton, self.experimentButton]