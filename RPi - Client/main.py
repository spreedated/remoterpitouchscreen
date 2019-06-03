#!/usr/bin/python
import os
#USE kivy.deps.sdl2 == 0.1.18 --- 0.1.20 is BROKEN! <-- colors are all wrong
#USE kivy.deps.gstreamer == 0.1.13 --- 0.1.14 is BROKEN! <-- took me about 3 hours if my life - 0.1.13 throws some error in console (which should have been fixed in 14 coming from broken symlinks- 14 actually fixed it, but there's no video), but at least it works... somehow
#USE ffpyplayer == 4.1.0 --- 4.2.0 is BROKEN! <-- took me about 3 hours if my life
if os.name == 'nt': #for Windows
	os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
	os.environ['KIVY_AUDIO'] = 'sdl2' # <-- seems more stable, but cannot play MP3, WAV only
	#os.environ['KIVY_AUDIO'] = 'gstplayer' # <-- can play WAV & MP3, also more accurate on timings, consider it a better alternative
	os.environ['KIVY_WINDOW'] = 'sdl2'
	os.environ['KIVY_IMAGE'] = 'sdl2'
	os.environ['KIVY_VIDEO'] = 'null' # use for debug, no video, no warnings in console
	#os.environ['KIVY_VIDEO'] = 'gstplayer' #using kivy.deps.gstreamer
	#os.environ['KIVY_VIDEO'] = 'ffpyplayer' #i dont like ffpyplayer
elif os.name == 'posix': #for RPi/Linux
	os.environ['KIVY_GL_BACKEND'] = 'gl'
	os.environ['KIVY_AUDIO'] = 'gstplayer'
	os.environ['KIVY_VIDEO'] = 'gstplayer'
#os.environ['KIVY_TEXT'] = 'sdl2'
#os.environ["KIVY_NO_CONFIG"] = "0" # BROKEN -- produces an error(no input at all) on rpi touchdisplay # DONT USE
os.environ["KIVY_NO_FILELOG"] = "1" # No spam
import sys
import kivy
kivy.require('1.10.1')
from kivy.config import Config
if os.name == 'nt':
	Config.set('graphics', 'show_cursor', '1')
	Config.set('graphics', 'fullscreen', 'false')
	Config.set('graphics', 'multisamples', '9')
elif os.name == 'posix':
	Config.set('graphics', 'fullscreen', 'true')
	Config.set('graphics', 'multisamples', '0') # disable AA for better performance
	Config.set('graphics', 'show_cursor', '0')
Config.set('kivy', 'exit_on_escape', '1') # Exit with escape key
Config.set('kivy', 'keyboard_mode', 'systemanddock') # or 'systemandmulti' - still no real difference here
Config.set('kivy','keyboard_layout', 'qwertz')
Config.set('kivy','pause_on_minimize', '0')
Config.set('kivy','window_icon','ico/icon.ico')
Config.set('kivy', 'show_fps', 1)
Config.set('graphics', 'window_state', 'normal')
Config.set('graphics', 'resizable', False)
# DEBUG
Config.set('modules', 'touchring', 'scale=0.1,alpha=1')
#Config.set('modules', 'monitor', '')
# ###
Config.write()
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.floatlayout import FloatLayout
from mod.Color import ColorConversion
from mod.Configuration import Configuration
from mod.Preload import PreloadAssets
from mod.Sound import Sounds
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from mod.Information import DynamicInformation
from cnt.LY_Background import *
from cnt.LY_StatusBars import *
from cnt.NV_MainNavigation import *
from cnt.PG_Welcome import *
import mod.Information as ApplicationInfo


if sys.version_info[0] != 3:
	print("This script requires Python version 3.x")
	sys.exit(1)

Config_LCARS = Configuration()
Preload_LCARS = PreloadAssets(Config_LCARS)
Info_LCARS = DynamicInformation()

class MainLayout(FloatLayout):
	shipinstance = None
	LY_TopStatusBar = None
	LY_BottomStatusBar = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#Background
		self.add_widget(LY_Background())
		#StatusBars
		self.LY_TopStatusBar = LY_TopStatusBar()
		self.add_widget(self.LY_TopStatusBar)
		self.LY_BottomStatusBar = LY_BottomStatusBar()
		self.add_widget(self.LY_BottomStatusBar)
		#Main Navigation
		self.add_widget(NV_MainNavigation(self, Config_LCARS, Preload_LCARS, self.LY_TopStatusBar, Info_LCARS))
		#Welcome Page
		self.add_widget(PG_Welcome(Config_LCARS, Preload_LCARS))

		Logger.info('INIT : Startup sequences finsihed - ' + ApplicationInfo.appFullName)

class MainApp(App):
	def build(self):
		self.title = ApplicationInfo.appFullName
		return MainLayout()

	def on_stop(self):
		Logger.info('EXIT : Made with <3')

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
