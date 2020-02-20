import glooey
import titi_tech.widgets.widgets as widgets


class ProjectTitle(glooey.Widget):
    custom_alignment = 'center'
    custom_left_padding = 10
    custom_right_padding = 10

    def __init__(self):
        super().__init__()

        hbox = glooey.HBox()
        self.title = widgets.Title("TitiTech")
        self.image = widgets.TitiImage()

        hbox.pack(self.title)
        hbox.add(self.image)
        hbox.set_padding(20)

        self._attach_child(hbox)


class LoginSubmitForm(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()

        hbox = glooey.HBox()
        self.login_text_form = widgets.TextForm("Password")

        self.login_button = widgets.DefaultButton("Login")

        hbox.pack(self.login_text_form)
        hbox.padding = 6
        hbox.add(self.login_button)

        self._attach_child(hbox)


class LoginPageWidget(glooey.Widget):
    custom_alignment = 'center'
    guest_button = None
    login_button = None

    def __init__(self, window_size):
        super().__init__()

        vbox = glooey.VBox()
        self.title = ProjectTitle()

        self.login_submit_form = LoginSubmitForm()

        self.guest_button = widgets.AltButton("Guest")
        self.login_button = self.login_submit_form.login_button
        self.text_form = self.login_submit_form.login_text_form

        vbox.pack(self.title)
        vbox.add(self.login_submit_form)
        vbox.add(self.guest_button)
        vbox.set_padding(all=window_size[1] / 20)

        self._attach_child(vbox)