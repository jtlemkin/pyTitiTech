from state import State
from button import Button
from States.sessionState import SessionState
from session import Session

from psychopy import event, gui

class SubjectSelectionState(State):
    subjectIDs = []
    subjectData = None
    session = None
    
    def on_load(self):
        super().on_load()
        
        self.addSubjectButton = Button(self.app.win, pos=(0, 0.5), size=(1, 0.5), text="Add Subject", on_click=self.addSubject)
        self.adminButton = Button(self.app.win, pos=(-0.5, -0.5), size=(1, 0.5), text="ADMIN", on_click=self.loginAdmin)
        self.selectButton = Button(self.app.win, pos=(0.5, -0.5), size=(1, 0.5), text="Select", on_click=self.startGoNoGo)
        
        self.subviews = [self.addSubjectButton, self.adminButton, self.selectButton]
        
        self.subjectData = self.app.fileManager.read_subject_data()
        
        for subject in self.subjectData:
            #subjects are represented as lists with the first element equal to the id
            self.subjectIDs.append(subject[0])
    
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
                 
    def isValidSubjectID(self, subjectInfo) -> None:
        idIsLongEnough = len(subjectInfo['ID']) >= 4
        
        return idIsLongEnough and subjectInfo['ID'] not in self.subjectIDs 
        
    def loginAdmin(self) -> None:
        adminInfo = {
            "Password" : ""
        }
        
        adminDlg = gui.DlgFromDict(adminInfo, sortKeys=False)
        
        if adminDlg.OK:
            if adminInfo["Password"] == "TitiC0d3!":
                self.app.transition_to("admin")
            else:
                print("Invalid password")
                
    def startGoNoGo(self) -> None:
        phases = ["Go Signal", "Wait Screen", "Alternating Stop Screen", "Random Stop Signal", "Experiment"]
        
        goNoGoSettings = {
            "subjectIDs" : self.subjectIDs,
            "Phase" : phases
        }
        
        subjectSelectDlg = gui.DlgFromDict(goNoGoSettings, sortKeys=False)
        
        if subjectSelectDlg.OK:
            selectedID = goNoGoSettings["subjectIDs"]
            selectedSubject = self.findSubjectFor(selectedID)
            
            self.session = Session(selectedSubject, goNoGoSettings["Phase"], self.app.fileManager)
            
            if self.settings_are_okay():
                if goNoGoSettings["Phase"] == "Go Signal":
                    self.app.transition_to("go_signal")
                else:
                    self.app.transition_to("session")
            
    def settings_are_okay(self):
        sessionState = {
            "Subject ID":  self.session.subject[0],
            "Subject Status" : self.session.subject[1],
            "Phase" : self.session.phase,
            "Negative Reinforcement Delay" : self.session.constants["negativeReinforcementDelay"],
            "Positive Reinforcement Delay" : self.session.constants["positiveReinforcementDelay"],
            "Hold Phase Delay" : self.session.constants["holdPhaseDelay"],
            "Session Timeout Time" : self.session.constants["sessionTimeoutTime"]
        }
        
        settingsOKDlg = gui.DlgFromDict(sessionState)
        
        return settingsOKDlg.OK
            
    def findSubjectFor(self, selectedID):
        for subject in self.subjectData:
            if subject[0] == selectedID:
                return subject
        
        return None
            
    def prepare_for_transition_to(self, newState) -> None:
        if isinstance(newState, SessionState):                
            newState.session = self.session