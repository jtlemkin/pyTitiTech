import glooey
from page import Page


class SSPageWidget(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()


class SSPage(Page):
    def __init__(self, app):
        self.title = "Select Subject"
        self.main_widget = SSPageWidget()

        super().__init__(app)

    def configure_buttons(self):
        pass
