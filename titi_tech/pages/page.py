class Page:
    main_widget = None
    previous_page_name = None
    title = None

    def __init__(self, app):
        self.app = app
        self.configure_buttons()

    def configure_buttons(self):
        pass