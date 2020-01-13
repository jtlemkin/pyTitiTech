from psychopy import visual

class Button:
    text = None
    
    def __init__(self, win, pos, size) -> None:
        self.win = win
        self.rect = visual.Rect(win, pos = pos, size = size, fillColor = 1, units="norm")
        
    def set_color(self, r: float, g: float, b: float) -> None:
        self.rect.setFillColor(color=(r,g,b), colorSpace='rgb')
        
    def set_text(self, text) -> None:
        print(self.rect.size[0])
        self.text = visual.TextStim(self.win, text, pos=self.rect.pos, units="norm", height=self.rect.size[1] * 0.15)
        
    def draw(self) -> None:
        self.rect.draw()
        
        if self.text:
            self.text.draw()