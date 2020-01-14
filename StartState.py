from state import State
from button import Button

from psychopy import visual
from psychopy import event

class StartState(State):
    
    context = None
    
    def __init__(self, win: visual.Window) -> None:
        self.addSubjectButton = Button(win, pos=(0, 0.5), size=(1, 0.5), text="Add Subject")
        self.adminButton = Button(win, pos=(-0.5, -0.5), size=(1, 0.5), text="ADMIN")
        self.selectButton = Button(win, pos=(0.5, -0.5), size=(1, 0.5), text="Select")
        
        self.background = visual.Rect(win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def draw(self) -> None:
        self.background.draw()
        
        self.addSubjectButton.draw()
        self.adminButton.draw()
        self.selectButton.draw()
        
    def handle_input(self) -> None:
        if self.addSubjectButton.has_been_clicked():
            print("click!")
            
        event.clearEvents()