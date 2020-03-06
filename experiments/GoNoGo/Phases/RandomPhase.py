from collections import deque
from random import randrange, shuffle

import psychtoolbox as ptb
from psychopy import visual, core, event, sound


#More than 4 in a row


class Signal:
    def __init__(self, _win, image):
        length_in_pixels = min(_win.size[0] / 2, _win.size[1])
        size = [length_in_pixels / _win.size[0], length_in_pixels / _win.size[1]]

        self.stim = visual.ImageStim(_win, image=image, units='norm', size=size)

    def move_left(self):
        self.stim.pos = [0.5, 0]

    def move_right(self):
        self.stim.pos = [-0.5, 0]

    def draw(self):
        self.stim.draw()

        win.flip()


win = visual.Window(fullscr=False, color="Black")
mouse = event.Mouse(win=win)

go_signal = Signal(win, image='../Assets/Images/goSignal.png')
no_go_signal = Signal(win, image='../Assets/Images/stopStimulus.png')

trial_sound = sound.Sound('../Assets/sounds/negativeReinforcement.wav')
good_click = sound.Sound('../Assets/sounds/negativeReinforcement.wav')
bad_click = sound.Sound('../Assets/sounds/negativeReinforcement.wav')


def draw(_signal, _is_signal_on_right):
    if is_signal_on_right:
        signal.move_right()
    else:
        signal.move_left()

    _now = ptb.GetSecs()
    trial_sound.play(when=_now + 0.1)

    core.wait(0.1 + 0.5)

    signal.draw()


num_consecutive_pos = 0
was_last_signal_on_right = False

is_go_signal = False

timer = core.CountdownTimer()

phases = [0 for _ in range(0, 10)] + [1 for _ in range(0, 10)]
shuffle(phases)
phases = deque(phases)


while phases:
    rand = randrange(0,2)
    is_signal_on_right = rand == 1

    if is_signal_on_right == was_last_signal_on_right:
        if num_consecutive_pos == 4:
            is_signal_on_right = not is_signal_on_right
            num_consecutive_pos = 0
        else:
            num_consecutive_pos += 1
    else:
        num_consecutive_pos = 0

    is_go_signal = phases.pop()

    if is_go_signal:
        signal = go_signal
    else:
        signal = no_go_signal

    draw(signal, is_signal_on_right)

    #How long is stim on screen?
    timer.reset(4.0)

    while timer.getTime() > 0:
        if mouse.getPressed()[0]:
            if mouse.isPressedIn(signal.stim) and is_go_signal:
                now = ptb.GetSecs()
                good_click.play(when=now + 0.01)

                win.flip()

                core.wait(7.5)
            else:
                now = ptb.GetSecs()
                bad_click.play(when=now + 0.01)

                win.flip()

                core.wait(4.5)

    win.flip()
