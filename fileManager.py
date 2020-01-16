class FileManager():
    def __init__(self, subject_file, constants_file):
        self.subject_file = subject_file
        self.constants_file = constants_file
    
    # Takes in an array of a subjects features
    def write_subject_data(self, data, replace = False, source = ""):
        if replace:
            subject_data = read_subject_data()
                
            for index, subject in enumerate(subject_data):
                #if subject id is equal to source id
                if subject[0] == source:
                   subject_data[index] = data
                   break
                        
                write_data = ""
                
                for subject in subject_data:
                    #Write id, condition, diameter as csv
                    write_data += f"{subject[0]},{subject[1]},{subject[2]}\n"
                    
                with open(self.subject_file, "w+"):
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
        
        with open(self.constants_file, "r") as f:
            for row in f.readlines():
                key_value_pair = row.split(",")
                key = key_value_pair[0]
                value = key_value_pair[1]
                
                if len(key_value_pair) == 2:
                    constants[key] = value
                    
        return constants
        