#!/usr/bin/python
import os
os.environ["KIVY_NO_FILELOG"] = "1"
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
os.environ['KIVY_AUDIO'] = 'sdl2' # <-- seems more stable, but cannot play MP3, WAV only
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_IMAGE'] = 'sdl2'
os.environ['KIVY_VIDEO'] = 'null' # use for debug, no video, no warnings in console

import sys
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
import math

Builder.load_string("""
<MainLayout>:
	size_hint: None,None
	size: 665,383
	pos: 118,49
""")

class MainLayout(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		x = Label(size=(330,30), size_hint=(None,None), pos=(self.pos[0],self.pos[1]))
		with x.canvas.before:
			Color(1,1,1,0.2)
			RoundedRectangle(size=x.size, size_hint=(None,None),  pos=x.pos, radius=(4,4,4,4))
		self.add_widget(x)

class MainApp(App):
	def build(self):
		self.title = 'Test'
		return MainLayout()

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
