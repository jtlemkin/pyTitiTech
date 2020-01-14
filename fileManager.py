class FileManager():
    def __init__(self, file_name):
        self.file_name = file_name
    
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
                    
                with open(self.file_name, "w+"):
                    f.write(write_data)
        else:
            #Write id, condition, diameter as csv
            with open(self.file_name, "a+") as f:
                f.write(f"{data[0]},{data[1]},{data[2]}\n")
                
    def read_subject_data(self):
        try: 
            f = open(self.file_name, "r")
            return [row.split(',') for row in f.readlines()]
        except FileNotFoundError:
            return []
        