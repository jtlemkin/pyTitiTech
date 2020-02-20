from psychopy import visual

from pyglet.text.document import UnformattedDocument
from pyglet.text.layout import IncrementalTextLayout
from pyglet.text.caret import Caret


class TextInput:
    def __init__(self, win, pos, width):
        self.document = UnformattedDocument('')
        self.document.set_style(0, len(self.document.text), dict(color=(0, 0, 0, 255)))
        font = self.document.get_font()
        height = font.ascent - font.descent

        self.layout = IncrementalTextLayout(self.document, width, height, multiline=False)
        self.caret = Caret(self.layout)

        self.layout.x = pos[0]
        self.layout.y = pos[1]

        pad = 0.1

        self.rect = visual.Rect(win, pos=pos, size=[width, height + 2 * pad], fillColor=(1,1,1), units="norm")

    def draw(self):
        self.rect.draw()
        self.layout.draw()

