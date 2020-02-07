from psychopy import visual, core, event, sound
import psychtoolbox as ptb


class GoSignal:
    def __init__(self, win):
        length_in_pixels = min(win.size[0], win.size[1])

        self.max_size = [2 * length_in_pixels / win.size[0], 2 * length_in_pixels / win.size[1]]
        self.min_size = [self.max_size[0] / 2, self.max_size[1] / 2]

        self.incr = [self.max_size[0] / 20, self.max_size[1] / 20]

        self.stim = visual.ImageStim(win, image='../Assets/goSignal.png', units='norm', size=self.max_size)

    def draw(self):
        self.stim.draw()

    def shrink(self):
        self.stim.size -= self.incr

        if self.is_too_small():
            self.stim.size = self.min_size

    def grow(self):
        self.stim.size += self.incr

        if self.is_too_big():
            self.stim.size = self.max_size

    def is_too_small(self):
        return self.stim.size[0] < self.min_size[0] or self.stim.size[1] < self.min_size[1]

    def is_too_big(self):
        return self.stim.size[0] > self.max_size[0] or self.stim.size[1] > self.max_size[1]

    def is_min_size(self):
        return self.stim.size[0] == self.min_size[0] and self.stim.size[1] == self.min_size[1]


class ClickHandler:
    def __init__(self, _go_signal, _good_click, _bad_click):
        self.num_good = 0
        self.num_bad = 0

        self.go_signal = _go_signal
        self.good_click_sound = _good_click
        self.bad_click_sound = _bad_click

    def on_good_click(self):
        self.num_bad = 0
        self.num_good += 1

        if self.num_good == 3:
            go_signal.shrink()

            self.num_good = 0

        now = ptb.GetSecs()
        good_click.play(when=now+0.5)

    def on_bad_click(self):
        self.num_good = 0
        self.num_bad += 1

        if self.num_bad == 3:
            go_signal.grow()

            self.num_bad = 0

        now = ptb.GetSecs()
        bad_click.play(when=now + 0.5)


win = visual.Window(fullscr=False, color="Black")
mouse = event.Mouse(win=win)

go_signal = GoSignal(win)

good_click = sound.Sound('../Assets/negativeReinforcement.wav')
bad_click = sound.Sound('../Assets/negativeReinforcement.wav')

click_handler = ClickHandler(go_signal, good_click, bad_click)


while not go_signal.is_min_size():
    go_signal.draw()
    win.flip()

    if mouse.getPressed()[0]:
        if mouse.isPressedIn(go_signal.stim):
            click_handler.on_good_click()
        else:
            click_handler.on_bad_click()

        core.wait(0.2)

    event.clearEvents()

