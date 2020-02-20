from psychopy.visual import Rect, TextStim


class Button:    
    def __init__(self, win, pos, size, on_click, fillColor = (0,0,0), text=None) -> None:
        self.rect = Rect(win, pos=pos, size=size, fillColor=fillColor, units="norm")

        text_pos = (pos[0] + 0.8, pos[1])

        self.text = TextStim(win, text, pos=text_pos, units="norm", height=self.rect.size[1] * 0.15)
        
        self.on_click = on_click
        
    def draw(self):
        self.rect.draw()
        
        if self.text:
            self.text.draw()
            
    def clicked_by(self, mouse):
        return mouse.isPressedIn(self.rect)