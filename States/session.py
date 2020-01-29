from datetime import datetime

class Session:
    def __init__(self, subject, phase, fileManager):
        this.subject = subject
        this.phase = phase
        this.fileManager = fileManager
        this.constants = fileManager.read_constants()
        
        this.start_time_stamp = datetime.now()
        
    def formatConstantsString(self):
        line = ""
        
        for key in constants:
            line += constants + ","
            
        return line[:-1]