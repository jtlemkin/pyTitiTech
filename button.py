from psychopy import visual, event

class Button:
    def __init__(self, win, pos, size, fillColor = (0,0,0), text=None) -> None:
        self.win = win
        self.rect = visual.Rect(win, pos = pos, size = size, fillColor = fillColor, units="norm")
        self.text = visual.TextStim(self.win, text, pos=self.rect.pos, units="norm", height=self.rect.size[1] * 0.15)
        
    def draw(self) -> None:
        self.rect.draw()
        
        if self.text:
            self.text.draw()
            
    def clicked_by(self, mouse: event.Mouse) -> bool:
        return mouse.isPressedIn(self.rect)
    