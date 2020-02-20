#!/usr/bin/env python3

import pyglet

pyglet.resource.path = ['../assets/images']
pyglet.resource.reindex()

from titi_tech.app import App

page_controller = App(page_name='login')

pyglet.app.run()