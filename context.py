from state import State

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