import glooey
import widgets
from page import Page


class ParameterFields(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()

        names = ["Name", "Status", "Phase", "Negative Reinforcement Delay",
                 "Positive Reinforcement Delay", "Hold Phase Delay", "Session Timeout Time",
                 "Stop Stimulus Duration", "Go Stimulus Duration", "Max Repeats"]

        labels = glooey.VBox()
        labels.set_padding(10)

        forms = glooey.VBox()
        forms.set_padding(10)

        buttons = glooey.VBox()
        buttons.set_padding(10)

        for i, name in enumerate(names):
            labels.add(widgets.Label(name, color='#000000'))
            forms.add(widgets.TextForm(name, width_hint=300))
            buttons.add(widgets.DefaultButton("Update"))

        hbox = glooey.HBox()
        hbox.add(labels)
        hbox.add(forms)
        hbox.add(buttons)

        self._attach_child(hbox)


class SSPageWidget(glooey.Widget):
    custom_alignment = 'center'
    custom_height_hint = 200

    def __init__(self):
        super().__init__()

        scroll_box = widgets.ScrollBox()

        grid = glooey.Grid()
        grid.set_width_hint(1000)
        grid.set_row_height(0, 500)
        grid.set_row_height(1, 75)

        self.default_button = widgets.DefaultButton("New Subject")
        #vbox.add(self.default_button)

        #scroll_box.add(vbox)

        #hbox = glooey.HBox()

        #hbox.add(scroll_box)

        self.parameter_fields = ParameterFields()

        grid[0, 0] = self.parameter_fields

        self.start_button = widgets.AltButton("Start Trial")

        grid[1, 0] = self.start_button

        self._attach_child(grid)


class SSPage(Page):
    def __init__(self, app):
        self.title = "Select Subject"
        self.main_widget = SSPageWidget()

        super().__init__(app)

    def configure_buttons(self):
        pass
