from state import State
from button import Button

import random
from state import State

from psychopy import core

class SessionState(State):
    session = None
    
    experiment_trial_type = []
    timeout_timer = None
    
    def on_load(self):
        super().on_load(self)
        
        if self.session.constants["phase"] == "Experiment":
            self.experiment_trial_type += [False for _ in range(0, 40)]
            self.experiment_trial_type += [True for _ in range(0, 20)]
            random.shuffle(self.experiment_trial_type)
            
            timeout_time = 24 * 60 * 60
        else:
            timeout_time = self.session.constants["sessionTimeoutTime"]
        
        self.timeout_timer = core.CountdownTimer(timeout_time)
        
        self.session.save()
        print("Constants: " + self.session.formatConstantsString())
        
    