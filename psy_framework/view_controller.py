from psychopy.visual import Window
from psy_framework.button import Button
from psy_framework.text_input import TextInput


class ViewController:
    app = None
    subviews = set()

    def draw(self):
        for view in self.subviews:
            view.draw()

    def add_subview(self, view):
        self.subviews.add(view)

    def add_button(self, pos, size="reg", text="Button", func=print):
        if size == "reg":
            size = [1, 0.5]

        button = Button(self.app.win, pos=pos, size=size, text=text, on_click=func)

        self.add_subview(button)

    def add_text_input(self, pos, width):
        text_input = TextInput(self.app.win, pos=pos, width=width)

        self.add_subview(text_input)
        
    # This function handles click events
    def handle_input(self):
        for view in self.subviews:
            if isinstance(view, Button) and view.clicked_by(self.app.mouse):
                view.on_click()

    # MARK: Lifecycle Methods

    def prepare_for_transition_to(self, new_state):
        pass
        
    def on_load(self):
        pass
        
    def on_appear(self):
        pass
        