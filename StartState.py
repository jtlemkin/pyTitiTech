from state import State
from button import Button
from fileManager import FileManager

from psychopy import visual, event, gui

class StartState(State):
    
    context = None
    fileManager = FileManager("subject-data.csv")
    
    subjectIDs = []
    subjectData = fileManager.read_subject_data()
    
    def __init__(self, win: visual.Window) -> None:
        self.addSubjectButton = Button(win, pos=(0, 0.5), size=(1, 0.5), text="Add Subject")
        self.adminButton = Button(win, pos=(-0.5, -0.5), size=(1, 0.5), text="ADMIN")
        self.selectButton = Button(win, pos=(0.5, -0.5), size=(1, 0.5), text="Select")
        
        self.background = visual.Rect(win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def draw(self) -> None:
        self.background.draw()
        
        self.addSubjectButton.draw()
        self.adminButton.draw()
        self.selectButton.draw()
        
    def handle_input(self) -> None:
        if self.addSubjectButton.has_been_clicked():
            self.addSubject()
    
    def addSubject(self) -> None:
        #762 is temp value for max diameter size
        subjectInfo = {"ID": "", "Condition": "", "Diameter" : 762}
        
        subjectDlg = gui.DlgFromDict(subjectInfo, sortKeys=False, fixed=['Diameter'])
            
        if subjectDlg.OK:
            if self.isValidSubjectID(subjectInfo):
                self.fileManager.write_subject_data(list(subjectInfo.values()))
                
                self.subjectIDs.append(subjectInfo["ID"])
                    
                 #this might not work
                self.subjectData.append(list(subjectInfo.values()))
            else:
                print("invalid subject")
                 
    def isValidSubjectID(self, subjectInfo):
        idIsLongEnough = len(subjectInfo['ID']) >= 4
        
        return idIsLongEnough and subjectInfo['ID'] not in self.subjectIDs       