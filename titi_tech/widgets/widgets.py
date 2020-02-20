import pyglet
import glooey
import titi_tech.colors as colors


class Label(glooey.Label):
    custom_font_name = 'Lato Regular'
    custom_font_size = 14
    custom_color = '#ffffff'
    custom_alignment = 'center'
    custom_left_padding = 10
    custom_right_padding = 10


class TextForm(glooey.Form):

    custom_alignment = 'fill'

    has_been_clicked = False

    def __init__(self, text=""):
        super().__init__(text)

        self.push_handlers(on_focus=self.remove_starting_text)

    def remove_starting_text(self, w):
        if not self.has_been_clicked:
            self.set_text('')
            self.has_been_clicked = True

    class Label(glooey.EditableLabel):
        custom_font_name = 'Lato Regular'
        custom_font_size = 16
        custom_color = '#000000'
        custom_width_hint = 200
        custom_left_padding = custom_font_size * 1
        custom_right_padding = custom_font_size * 1
        custom_top_padding = custom_font_size * 0.5
        custom_bottom_padding = custom_font_size * 0.5
        custom_selection_background_color = colors.complementary
        custom_unfocus_on_enter = True

    class Base(glooey.Background):
        custom_color = colors.primary_lightest


class ButtonLabel(glooey.Label):
    custom_font_size = 18
    custom_color = '#ffffff'
    custom_left_padding = custom_font_size * 1
    custom_right_padding = custom_font_size * 1
    custom_top_padding = custom_font_size * 0.5
    custom_bottom_padding = custom_font_size * 0.5
    custom_font_name = 'Lato Regular'
    custom_alignment = 'top'


class DefaultButton(glooey.Button):
    Foreground = ButtonLabel

    class Base(glooey.Background):
        custom_color = colors.primary

    class Down(glooey.Background):
        custom_color = colors.primary_down

    class Over(glooey.Background):
        custom_color = colors.primary_hover


class AltButton(glooey.Button):
    Foreground = ButtonLabel

    class Base(glooey.Background):
        custom_color = colors.complementary

    class Down(glooey.Background):
        custom_color = colors.complementary_down

    class Over(glooey.Background):
        custom_color = colors.complementary_hover


class Header(glooey.Background):
    custom_alignment = 'fill top'
    custom_color = '#3A98FE'
    custom_height_hint = 50

    def __init__(self, title='', **kwargs):
        super().__init__(**kwargs)

        self.title = Label(title)
        self._attach_child(self.title)


class Title(glooey.Label):
    custom_font_name = 'futura'
    custom_font_size = 40
    custom_color = '#000000'
    custom_alignment = 'center'


class TitiImage(glooey.Background):
    titi_image = pyglet.resource.image('TitiMonkeys.png')
    titi_image.height = 125
    titi_image.width = 125

    custom_image = titi_image