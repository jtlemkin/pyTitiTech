from datetime import datetime

class Session:
    def __init__(self, subject, phase, fileManager):
        self.subject = subject
        self.phase = phase
        self.fileManager = fileManager
        self.constants = fileManager.read_constants()
        
        self.start_time_stamp = datetime.now()
        
    def formatConstantsString(self):
        line = ""
        
        for key in constants:
            line += constants + ","
            
        return line[:-1]