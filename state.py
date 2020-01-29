from psychopy import visual

from button import Button

class State():
    app = None
    background = None
    subviews = []
        
    def draw(self):
        self.background.draw()
        
        for view in self.subviews:
            view.draw()
        
    #This function handles click events    
    def handle_input(self):
        for view in self.subviews:
            if isinstance(view, Button) and view.clicked_by(self.app.mouse):
                view.on_click()
        
    def prepare_for_transition_to(self, newState):
        pass
        
    def on_load(self):        
        self.background = visual.Rect(self.app.win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def on_appear(self):
        pass
        