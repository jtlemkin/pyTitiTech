from psychopy import visual, core, event, sound
import psychtoolbox as ptb
from random import randrange


class GoSignal:
    def __init__(self, _win):
        length_in_pixels = min(_win.size[0] / 2, _win.size[1])
        size = [length_in_pixels / _win.size[0], length_in_pixels / _win.size[1]]

        self.stim = visual.ImageStim(_win, image='../Assets/Images/goSignal.png', units='norm', size=size)

    def move_left(self):
        self.stim.pos = [0.5, 0]

    def move_right(self):
        self.stim.pos = [-0.5, 0]

    def draw(self):
        self.stim.draw()

        win.flip()


win = visual.Window(fullscr=False, color="Black")
mouse = event.Mouse(win=win)

go_signal = GoSignal(win)
trial_sound = sound.Sound('../Assets/Sounds/negativeReinforcement.wav')
good_click = sound.Sound('../Assets/Sounds/negativeReinforcement.wav')
bad_click = sound.Sound('../Assets/Sounds/negativeReinforcement.wav')

num_consecutive = 0
was_last_signal_on_right = -1

timer = core.CountdownTimer()


def draw_signal(_is_signal_on_right):
    if is_signal_on_right:
        go_signal.move_right()
    else:
        go_signal.move_left()

    _now = ptb.GetSecs()
    trial_sound.play(when=_now + 0.1)

    core.wait(0.1 + 0.5)

    go_signal.draw()


for _ in range(0, 20):
    rand = randrange(0,2)
    is_signal_on_right = rand == 1

    if is_signal_on_right == was_last_signal_on_right:
        if num_consecutive == 4:
            is_signal_on_right = not is_signal_on_right
            num_consecutive = 0
        else:
            num_consecutive += 1
    else:
        num_consecutive = 0

    was_last_signal_on_right = is_signal_on_right

    draw_signal(is_signal_on_right)

    #How long is stim on screen?
    timer.reset(4.0)

    while timer.getTime() > 0:
        if mouse.getPressed()[0]:
            win.flip()

            if mouse.isPressedIn(go_signal.stim):
                now = ptb.GetSecs()
                good_click.play(when=now + 0.1)

                core.wait(7.5)
            else:
                now = ptb.GetSecs()
                bad_click.play(when=now + 0.1)

                core.wait(4.5)

    win.flip()







