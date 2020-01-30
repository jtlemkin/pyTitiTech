from state import State
from button import Button

from psychopy import visual, event, gui

class AdminState(State):
    subjectIDs = []
    subjectData = None
    
    def on_load(self):
        super().on_load()
        
        self.editConfigsButton = Button(self.app.win, pos=(0, 0.5), size=(1, 0.5), text="Edit configs", on_click=self.configureSettings)
        self.dataFileManagementButton = Button(self.app.win, pos=(-0.5,0), size=(1, 0.5), text="Data Management", on_click=self.transition_to_google_drive_state)
        self.subjectDataButton = Button(self.app.win, pos=(0.5, 0), size=(1, 0.5), text="Subject Data", on_click=self.manageSubjects)
        self.exitButton = Button(self.app.win, pos=(0, -0.5), size=(1, 0.5), text="Exit", fillColor=(1,0,0), on_click=self.return_to_start)
        
        self.subviews = [self.editConfigsButton, self.dataFileManagementButton, self.subjectDataButton, self.exitButton]
        
        self.subjectData = self.app.fileManager.read_subject_data()
        
        for subject in self.subjectData:
            #subjects are represented as lists with the first element equal to the id
            self.subjectIDs.append(subject[0])
            
    def return_to_start(self):
        self.app.transition_to("start")
    
    def configureSettings(self):        
        constants = self.app.fileManager.read_constants()
        
        configGui = gui.DlgFromDict(constants, sortKeys = False)
        
        if configGui.OK:
            self.app.fileManager.write_constants(constants)
            
    def manageSubjects(self):
        subject = self.selectSubject()
        self.updateSubject(subject)    
            
    def selectSubject(self):
        subjects = {
            "Subjects" : self.subjectIDs
        }
        
        subjectSelectGui = gui.DlgFromDict(subjects, sortKeys = False)
        
        if subjectSelectGui.OK:
            subject = self.findSubjectFor(subjects["Subjects"])
            return subject
            
    def findSubjectFor(self, selectedID):
        for subject in self.subjectData:
            if subject[0] == selectedID:
                return subject
        
        return None
        
    def updateSubject(self, subject):
        subjectInfo = {
            "ID" : subject[0],
            "Status" : subject[1]
        }
        
        updateSubjectDlg = gui.DlgFromDict(subjectInfo, sortKeys = False)
        
        if updateSubjectDlg.OK:
            for i, subject in enumerate(self.subjectData):
                if subject[0] == subjectInfo["ID"]:
                    self.subjectData[i][1] = subjectInfo["Status"]
                    
            self.app.fileManager.write_subject_data(self.subjectData, overwrite = True)
            
    def transition_to_google_drive_state(self):
        self.app.transition_to("google_drive")
