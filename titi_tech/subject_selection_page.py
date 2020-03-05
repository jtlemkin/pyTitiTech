import glooey
import widgets
from page import Page


class SSPageWidget(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()

        hbox = glooey.HBox()

        hbox.add(widgets.DefaultButton("Add new subject"))
        hbox.add(widgets.AltButton("Use existing subject"))

        self._attach_child(hbox)


class SSPage(Page):
    def __init__(self, app):
        self.title = "Subject Selection"

        super().__init__(app)

        self.main_widget = SSPageWidget()
