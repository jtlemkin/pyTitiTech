from psychopy import visual
from Framework.button import Button


class PsyViewController:
    app = None
    background = None
    subviews = set()

    def draw(self):
        self.background.draw()
        
        for view in self.subviews:
            view.draw()

    def add_subview(self, view):
        self.subviews.add(view)

    def add_button(self, pos, size, text, func):
        button = Button(self.app.win, pos=pos, size=size, text=text, on_click=func)

        self.add_subview(button)
        
    # This function handles click events
    def handle_input(self):
        for view in self.subviews:
            if isinstance(view, Button) and view.clicked_by(self.app.mouse):
                view.on_click()

    # MARK: Lifecycle Methods

    def prepare_for_transition_to(self, newState):
        pass
        
    def on_load(self):        
        self.background = visual.Rect(self.app.win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def on_appear(self):
        pass
        