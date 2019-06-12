#!/usr/bin/python
import os
import sys
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
			on_press: App.get_contents().stop()

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

class MenuScreen(Screen):
	pass

class SettingsScreen(Screen):
	pass

class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.size = (800,480)
		self.size_hint = (None,None)
		self.pos = (0,0)


class ScreenManagement(ScreenManager):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.add_widget(MenuScreen(name='menu'))
		#self.add_widget(SettingsScreen(name='settings'))

		self.size = (400,400)
		self.size_hint = (None,None)

		self.add_widget(MainLayout)

sm = ScreenManagement()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class MainApp(App):
	def build(self):
		self.title = 'Test'
		return ScreenManagement()

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
