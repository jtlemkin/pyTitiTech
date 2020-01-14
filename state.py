from abc import ABC

class State(ABC):
    
    def context(self):
        return self.context
        
    def context(self, context) -> None:
        self.context = context
        
    def draw(self) -> None:
        pass
        
    def handle_input(self) -> None:
        pass