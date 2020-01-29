from datetime import datetime

class Session:
    def __init__(self, subject, phase, fileManager):
        self.subject = subject
        self.phase = phase
        self.fileManager = fileManager
        self.constants = fileManager.read_constants()
        
        self.start_time_stamp = datetime.now()
        
    def formatConstantsString(self):
        line = self.start_time_stamp + ','
        line += self.subject[0] + ','
        line += self.subject[1] + ','
        line += self.phase + ',' #Should be a raw value
        line += self.constants["goStimulusDuration"] + ','
        line += self.constants["stopStiumulusDuration"] + ','
        line += self.constants["negativeReinforcementDelay"] + ','
        line += self.constants["postivieReinforcementDelay"] + ','
        line += self.constants["holdPhaseDelay"] + ','
        line += self.constants["sessionTimeoutTime"] + '\n'
        
        return line
