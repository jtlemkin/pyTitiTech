import pyglet
import glooey

from titi_tech.pages.login_page import LoginPage
import titi_tech.widgets.widgets as widgets
import titi_tech.colors as colors


class App:
    window = pyglet.window.Window()
    window_size = window.get_size()

    gui = glooey.Gui(window)
    header = widgets.Header()
    page = None

    pages = {
        "login": LoginPage,
        "subject_selection": LoginPage
    }

    def __init__(self, page_name):
        self.gui.add(glooey.Background(color=colors.background))
        self.gui.add(self.header)

        self.transition_to(page_name)

    def transition_to(self, page_name):
        print(f"Transitioning to {page_name}")

        if self.page:
            self.gui.remove(self.page.main_widget)

        self.page = self.pages[page_name](self)
        self.gui.add(self.page.main_widget)

        self.update_header()

    def update_header(self):
        if self.page.title:
            self.header.title.set_text(self.page.title)