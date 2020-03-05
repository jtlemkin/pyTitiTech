import colors as colors
import glooey
import pyglet
import widgets as widgets
from login_page import LoginPage
from subject_selection_page import SSPage


class App:
    window = pyglet.window.Window(fullscreen=False, height=780, width=1200)
    window_size = window.get_size()

    layout = glooey.VBox()

    gui = glooey.Gui(window)
    header = widgets.Header()
    page = None

    pages = {
        "login": LoginPage,
        "subject_selection": SSPage
    }

    def __init__(self, page_name):
        self.gui.add(glooey.Background(color=colors.background))
        self.transition_to(page_name)

    def transition_to(self, page_name):
        print(f"Transitioning to {page_name}")

        if self.page:
            self.gui.remove(self.layout)

        self.page = self.pages[page_name](self)
        self.header = widgets.Header(self.page.title)

        self.layout = glooey.VBox()
        self.layout.pack(self.header)
        self.layout.add(self.page.main_widget)

        self.gui.add(self.layout)
