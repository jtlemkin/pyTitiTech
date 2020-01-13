from abc import ABC

class State(ABC):
    
    def context(self):
        return self.context
        
    def context(self, context) -> None:
        self.context = context
        
    def draw(self) -> None:
        pass