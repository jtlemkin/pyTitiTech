import glooey
import widgets
from page import Page


class SSPageWidget(glooey.Widget):
    custom_alignment = 'center'

    add_subject_button = widgets.DefaultButton("Add new subject")
    use_existing_subject_button = widgets.AltButton("Use existing subject")

    def __init__(self):
        super().__init__()

        hbox = glooey.HBox()

        hbox.add(self.add_subject_button)
        hbox.add(self.use_existing_subject_button)

        self._attach_child(hbox)


class SSPage(Page):
    def __init__(self, app):
        self.title = "Select Subject"
        self.main_widget = SSPageWidget()

        super().__init__(app)

    def configure_buttons(self):
        self.main_widget.add_subject_button.push_handlers(on_click=lambda x: self.app.transition_to('add_subject'))
        pass
