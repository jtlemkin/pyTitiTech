from Framework.state import State

import random

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
        
        self.timeout_timer = core.Clock(timeout_time)
        
        self.session.save()
        print("Configuration: " + self.session.formatConstantsString())
        
    def on_appear(self):
        super().on_appear(self)
        
        self.session.trial.timeout_timer = None
        #invalidate buttons
        
        core.wait(1)
        
        if session:
            self.run_trial()
            
    def run_trial(self):
        #If session ends before the trial would, don't create a trial
        #Don't start the trial if running experiment?
        
        if self.session.constants.phase != "Experiment" and self.session.get_remaining_session_time() < 6.0:
            pass
    