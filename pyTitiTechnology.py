#exec(open('pyTitiTechnology.py').read())

from psychopy import visual
from context import Context
from startState import StartState

win = visual.Window(size=(800,600))

context = Context(StartState(win))

while True:
    context.state.draw()
    context.state.handle_input()
    win.flip()