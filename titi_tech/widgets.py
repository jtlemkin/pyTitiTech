import colors as colors
import glooey


class Label(glooey.Label):
    custom_font_name = 'Lato Regular'
    custom_font_size = 14
    custom_color = '#ffffff'
    custom_alignment = 'left'
    custom_left_padding = 10
    custom_right_padding = 10


class TextForm(glooey.Form):
    custom_alignment = 'fill'

    has_been_clicked = False

    def __init__(self, text="", width_hint=400):
        super().__init__(text)

        self.push_handlers(on_focus=self.remove_starting_text)

        self.get_label().set_width_hint(width_hint)

    def remove_starting_text(self, w):
        if not self.has_been_clicked:
            self.set_text('')
            self.has_been_clicked = True

    class Label(glooey.EditableLabel):
        custom_font_name = 'Lato Regular'
        custom_font_size = 14
        custom_color = '#000000'
        custom_width_hint = 400
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


class Header(glooey.Frame):
    custom_alignment = 'fill top'
    custom_height_hint = 60

    Box = glooey.Grid

    class Decoration(glooey.Background):
        custom_color = colors.primary
        pass

    def __init__(self, title='', **kwargs):
        super().__init__(**kwargs)

        self.add(col=1, widget=Title(title))
        self.add(col=2, widget=glooey.Background())

    def add(self, widget, col, row=0):
        self.box.add(row, col, widget)


class Title(glooey.Label):
    custom_font_name = 'futura'
    custom_font_size = 24
    custom_color = '#ffffff'
    custom_alignment = 'center'


class ScrollBox(glooey.ScrollBox):
    custom_alignment = 'center'

    class Frame(glooey.Frame):

        class Decoration(glooey.Background):
            #custom_color = colors.primary_lightest
            custom_width_hint = 500

        Box = glooey.Bin

    class VBar(glooey.VScrollBar):

        class Decoration(glooey.Background):
            custom_height_hint = 200
            custom_width_hint = 10
            custom_color = colors.complementary

        #Forward = glooey.Placeholder
        class Forward(glooey.Button):
            custom_width_hint = 25
            custom_height_hint = 25
            custom_color = colors.complementary_down

        #Backward = glooey.Placeholder
        class Backward(glooey.Button):
            custom_width_hint = 25
            custom_height_hint = 25
            custom_color = colors.complementary_hover

        #Grip = glooey.Placeholder
        class Grip(glooey.Background):
            custom_width_hint = 10
            custom_height_hint = 50
            custom_color = colors.primary_down


class Field(glooey.Widget):
    custom_alignment = 'left'

    def __init__(self, title=''):
        super().__init__()

        self.label = Label(title, color='#000000')
        self.text_form = TextForm(title, width_hint=300)
        self.button = DefaultButton("Update")

        hbox = glooey.HBox()
        hbox.pack(self.label)
        hbox.add(self.text_form)
        hbox.add(self.button)

        self._attach_child(hbox)