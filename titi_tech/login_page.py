import glooey
import pyglet

import widgets
from page import Page


class TitiImage(glooey.Background):
    titi_image = pyglet.resource.image('TitiMonkeys.png')
    titi_image.height = 300
    titi_image.width = titi_image.height

    custom_image = titi_image


class ProjectTitle(glooey.Widget):
    custom_alignment = 'center'
    custom_left_padding = 10
    custom_right_padding = 10
    custom_bottom_padding = 50

    def __init__(self):
        super().__init__()

        hbox = glooey.HBox()
        #self.title = widgets.Title("Admin Login")
        self.image = TitiImage()

        #hbox.pack(self.title)
        hbox.add(self.image)
        hbox.set_padding(20)

        self._attach_child(hbox)


class LoginSubmitForm(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()

        hbox = glooey.HBox()
        self.login_text_form = widgets.TextForm("Enter Password")

        self.login_button = widgets.DefaultButton("Admin Login")

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

        self.guest_button = widgets.AltButton("Guest Login")
        self.login_button = self.login_submit_form.login_button
        self.text_form = self.login_submit_form.login_text_form

        vbox.pack(self.title)
        vbox.add(self.login_submit_form)
        vbox.add(self.guest_button)
        vbox.set_padding(all=window_size[1] / 20)

        self._attach_child(vbox)


class LoginPage(Page):
    title = "Bales Lab"

    def __init__(self, app):
        self.main_widget = LoginPageWidget(app.window_size)
        self.guest_button = self.main_widget.guest_button
        self.login_button = self.main_widget.login_button

        super().__init__(app)

    def configure_buttons(self):
        self.guest_button.push_handlers(on_click=lambda x: self.app.transition_to('select_subject'))
        self.login_button.push_handlers(on_click=lambda x: self.app.transition_to('select_subject'))
