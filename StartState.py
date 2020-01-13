from state import State
from button import Button

from psychopy import visual

class StartState(State):
    
    context = None
    
    def __init__(self, win: visual.Window) -> None:
        self.addSubjectButton = Button(win, pos=(0, 0.5), size=(1, 0.5))
        self.addSubjectButton.set_color(0, 0, 0)
        self.addSubjectButton.set_text("Add Subject")
        
        self.adminButton = Button(win, pos=(-0.5, -0.5), size=(1, 0.5))
        self.adminButton.set_color(0, 0, 0)
        self.adminButton.set_text("ADMIN")
        
        self.selectButton = Button(win, pos=(0.5, -0.5), size=(1, 0.5))
        self.selectButton.set_color(0, 0, 0)
        self.selectButton.set_text("Select")
        
        self.background = visual.Rect(win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def draw(self) -> None:
        self.background.draw()
        self.addSubjectButton.draw()
        self.adminButton.draw()
        self.selectButton.draw()