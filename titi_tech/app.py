import pyglet
import glooey

from titi_tech.pages.login import LoginPage
import titi_tech.widgets as widgets
import titi_tech.colors as colors


class App:
    window = pyglet.window.Window()
    window_size = window.get_size()

    gui = glooey.Gui(window)
    page = None

    def __init__(self, page_name):
        self.gui.add(glooey.Background(color=colors.background))
        self.gui.add(widgets.Header())

        self.transition_to(page_name)

    def transition_to(self, page_name):
        print(f"Transitioning to {page_name}")

        pages = {
            "login" : LoginPage
        }

        if self.page:
            self.gui.remove(self.page)

        self.page = pages[page_name](self.window_size)
        self.gui.add(self.page)