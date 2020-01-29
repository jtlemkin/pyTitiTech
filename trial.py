class Trial():
    def __init__(self, constants):
        self.touched = False
        self.timeout_timer = None
        self.hold_state_touch_counter = 0
        self.stimulus_history = []
        self.response_time_timer = None
        self.trial_number = 0
        self.hit = false
        
        self.constants = constants