class StartState(State, win):
    
    def __init__(self) -> None:
        addSubjectButton = Button(win, pos=(0, 100), size=(100, 100))
        addSubjectButton.set_text("Add Subject")
        
        adminButton = Button(win, pos(-100, -100), size=(100, 100))
        adminButton.set_text("ADMIN")
        
        selectButton = Button(win, pos(100, -100), size=(100,100))
        selectButton.set_text("Select")
        
        win.color = (0, 0, 1)