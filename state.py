from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    This class manages the different states that our application can be in
    e.g. Transition between start state to trial state
    """
    
    state = None
    
    def __init__(self, state: State) -> None:
        self.transition_to(state)
        
    def transition_to(self, state: State):
        self.state = state
        self.state.context = self
        
        
class State(ABC):
    
    @property
    def context(self) -> Context:
        return self.context
        
    @context.setter
    def context(self, context: Context) -> None:
        self.context = context
        
    @abstractmethod
    def display(self) -> None:
        pass