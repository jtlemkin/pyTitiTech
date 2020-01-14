from psychopy import visual, event

class Button:
    def __init__(self, win, pos, size, text=None) -> None:
        self.win = win
        self.rect = visual.Rect(win, pos = pos, size = size, fillColor = (0,0,0), units="norm")
        self.text = visual.TextStim(self.win, text, pos=self.rect.pos, units="norm", height=self.rect.size[1] * 0.15)
        
    def set_color(self, r: float, g: float, b: float) -> None:
        self.rect.setFillColor(color=(r,g,b), colorSpace='rgb')
        
    def draw(self) -> None:
        self.rect.draw()
        
        if self.text:
            self.text.draw()
            
    def has_been_clicked(self) -> bool:
        return event.Mouse().isPressedIn(self.rect)
    