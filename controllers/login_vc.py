from psy_framework.view_controller import ViewController


class LoginViewController(ViewController):
    def on_load(self):
        self.add_text_input(pos=(0,0.5), width=0.5)
        self.add_button(pos=(0, -0.5), text="Guest", func=self.login_as_guest)

    def login_as_guest(self):
        pass
