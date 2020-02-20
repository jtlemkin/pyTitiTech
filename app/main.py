#!/usr/bin/env python3

import pyglet

pyglet.resource.path = ['../assets/images']
pyglet.resource.reindex()

import glooey
from app.pages.login import LoginPage
import app.colors as colors
import app.widgets as widgets

window = pyglet.window.Window()
gui = glooey.Gui(window)

window_size = window.get_size()
print(window_size)

gui.add(glooey.Background(color=colors.background))
gui.add(widgets.Header())
gui.add(LoginPage(window_size))

pyglet.app.run()