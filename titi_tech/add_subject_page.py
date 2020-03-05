import glooey
from page import Page


class ASPageWidget(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()


class ASPage(Page):
    def __init__(self, app):
        self.title = "Add Subject"

        super().__init__(app)

        self.main_widget = glooey.Placeholder()