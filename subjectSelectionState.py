from state import State
from button import Button

from psychopy import visual, event, gui

class SubjectSelectionState(State):
    
    def __init__(self, app) -> None:
        self.app = app
        
        self.addSubjectButton = Button(app.win, pos=(0, 0.5), size=(1, 0.5), text="Add Subject")
        self.adminButton = Button(app.win, pos=(-0.5, -0.5), size=(1, 0.5), text="ADMIN")
        self.selectButton = Button(app.win, pos=(0.5, -0.5), size=(1, 0.5), text="Select")
        
        self.subjectIDs = []
        self.subjectData = subjectData = app.fileManager.read_subject_data()
        
        self.background = visual.Rect(app.win, size=(4,4), units='norm')
        self.background.color = (0, 0, 1)
        
    def draw(self) -> None:
        self.background.draw()
        
        self.addSubjectButton.draw()
        self.adminButton.draw()
        self.selectButton.draw()
        
    def handle_input(self) -> None:
        if self.addSubjectButton.clicked_by(self.app.mouse):
            self.addSubject()
        elif self.adminButton.clicked_by(self.app.mouse):
            self.loginAdmin()
            
        event.clearEvents()
    
    def addSubject(self) -> None:
        #762 is temp value for max diameter size
        subjectInfo = {"ID": "", "Condition": "", "Diameter" : 762}
        
        subjectDlg = gui.DlgFromDict(subjectInfo, sortKeys=False, fixed=['Diameter'])
            
        if subjectDlg.OK:
            if self.isValidSubjectID(subjectInfo):
                self.app.fileManager.write_subject_data(list(subjectInfo.values()))
                
                self.subjectIDs.append(subjectInfo["ID"])
                    
                self.subjectData.append(list(subjectInfo.values()))
            else:
                print("invalid subject")
                 
    def isValidSubjectID(self, subjectInfo):
        idIsLongEnough = len(subjectInfo['ID']) >= 4
        
        return idIsLongEnough and subjectInfo['ID'] not in self.subjectIDs 
        
    def loginAdmin(self):
        adminInfo = {
            "Password" : ""
        }
        
        adminDlg = gui.DlgFromDict(adminInfo, sortKeys=False)
        
        if adminDlg.OK:
            if adminInfo["Password"] == "TitiC0d3!":
                self.app.transition_to("admin")
            else:
                print("Invalid password")