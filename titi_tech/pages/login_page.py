import titi_tech.widgets.login_widgets as login_widgets
from titi_tech.pages.page import Page


class LoginPage(Page):
    def __init__(self, app):
        self.main_widget = login_widgets.LoginPageWidget(app.window_size)
        self.guest_button = self.main_widget.guest_button
        self.login_button = self.main_widget.login_button

        super().__init__(app)

    def configure_buttons(self):
        self.guest_button.push_handlers(on_click=lambda x: self.app.transition_to('subject_selection'))
        self.login_button.push_handlers(on_click=lambda x: self.app.transition_to('subject_selection'))