class FileManager():
    def __init__(self, subject_file, constants_file):
        self.subject_file = subject_file
        self.constants_file = constants_file
    
    # Takes in an array of a subjects features
    def write_subject_data(self, data, overwrite = False):
        if overwrite:
            subject_data = self.read_subject_data()
            
            write_data = ''.join([f"{subject[0]},{subject[1]},{subject[2]}\n" for subject in subject_data])
                    
            with open(self.subject_file, "w+") as f:
               f.write(write_data)
        else:
            #Write id, condition, diameter as csv
            with open(self.subject_file, "a+") as f:
                f.write(f"{data[0]},{data[1]},{data[2]}\n")
                
    def read_subject_data(self):
        try: 
            f = open(self.subject_file, "r")
            return [row.split(',') for row in f.readlines()]
        except FileNotFoundError:
            return []
            
    def read_constants(self):
        constants = {}
        
        try:
            f = open(self.constants_file, "r")
            
            line_no = 1
            for row in f.readlines():
                if line_no > 7:
                    break
                    
                line_no += 1
                
                key_value_pair = row.split(",")
                key = key_value_pair[0]
                value = key_value_pair[1]
                    
                if len(key_value_pair) == 2:
                    constants[key] = float(value[:-1])
                
            f.close()
        except FileNotFoundError:
            #Return default values for configs
            constants["negativeReinforcementDelay"] = 3.0
            constants["positiveReinforcementDelay"] = 1.0
            constants["holdPhaseDelay"] = 1.5
            constants["sessionTimeoutTime"] = 480
            constants["stopStimulusDuration"] = 1.0
            constants["goStimulusDuration"] = 30
            constants["maxRepeats"] = 4
                    
        return constants
        
    def write_constants(self, constants):
        with open(self.constants_file, "w+") as f:
            for key in constants:
                f.write(f"{key},{constants[key]}\n")
        