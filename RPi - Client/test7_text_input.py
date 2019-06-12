#!/usr/bin/python
import os

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

Builder.load_string("""
<MainLayout>:
	size_hint: None,None
	size: 800,480
	pos: 0,0
""")

class MainLayout(FloatLayout):
	textinput = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.textinput = TextInput(text='Hello world', size=(500,25), size_hint=(None,None), pos=(50,300), multiline=False, password=True, password_mask='#')
		self.add_widget(self.textinput)

		btn = Button(size=(100,25), size_hint=(None,None), pos=(600,300), text='send')
		btn.bind(on_press=self.printme)
		self.add_widget(btn)

	def printme(self, instance):
		print(self.textinput.text)

class MainApp(App):
	def build(self):
		self.title = 'Test'
		return MainLayout()

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
