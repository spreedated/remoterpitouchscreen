#!/usr/bin/python
import os
#USE kivy.deps.sdl2 == 0.1.18 --- 0.1.20 is BROKEN! <-- colors are all wrong
#USE kivy.deps.gstreamer == 0.1.13 --- 0.1.14 is BROKEN! <-- took me about 3 hours if my life - 0.1.13 throws some error in console (which should have been fixed in 14 coming from broken symlinks- 14 actually fixed it, but there's no video), but at least it works... somehow
#USE ffpyplayer == 4.1.0 --- 4.2.0 is BROKEN! <-- took me about 3 hours if my life
if os.name == 'nt': #for Windows
	os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
	#os.environ['KIVY_AUDIO'] = 'sdl2' # <-- seems more stable, but cannot play MP3, WAV only
	os.environ['KIVY_AUDIO'] = 'gstplayer' # <-- can play WAV & MP3, also more accurate on timings, consider it a better alternative
	os.environ['KIVY_WINDOW'] = 'sdl2'
	os.environ['KIVY_IMAGE'] = 'sdl2'
	#os.environ['KIVY_VIDEO'] = 'null' # use for debug, no video, no warnings in console
	os.environ['KIVY_VIDEO'] = 'gstplayer' #using kivy.deps.gstreamer
	#os.environ['KIVY_VIDEO'] = 'ffpyplayer' #i dont like ffpyplayer
elif os.name == 'posix': #for RPi/Linux
	os.environ['KIVY_GL_BACKEND'] = 'gl'
	os.environ['KIVY_AUDIO'] = 'gstplayer'
	os.environ['KIVY_VIDEO'] = 'gstplayer'
os.environ['KIVY_TEXT'] = 'sdl2'
#os.environ["KIVY_NO_CONFIG"] = "0" # BROKEN -- produces an error(no input at all) on rpi touchdisplay # DONT USE
os.environ["KIVY_NO_FILELOG"] = "1" # No spam
import sys
import random
import datetime
import pprint
import time
#inara
import requests
from lxml import html
# ###
import threading
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
Config.set('modules', 'monitor', '')
# ###
Config.write()
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
#from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.relativelayout import RelativeLayout
#from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from kivy.core.video import VideoBase
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.scrollview import ScrollView
from mod.Color import ColorConversion
from mod.StatusBars import *
from mod.Inara_Ships import Ships
from mod.Configuration import Configuration
from mod.Preload import PreloadAssets
from mod.Sound import Sounds
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from mod.API_Works import Inara

if sys.version_info[0] != 3:
	print("This script requires Python version 3.x")
	sys.exit(1)

Config_LCARS = Configuration()
Preload_LCARS = PreloadAssets()

class MainLayout(FloatLayout):
	shipinstance = None
	TopStatusBar = None
	BottomStatusBar = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		bg = Image(texture=Preload_LCARS.returnPreloadedAsset('bg.png'), pos=(1,0), size_hint=(None,None), size=(800,480), id='background')
		self.add_widget(bg)
		txt_menu = Label(text='MENU', pos=(42,435), size=(35,18), size_hint=(None,None), color=(0,0,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28 sp')
		self.add_widget(txt_menu)

		self.TopStatusBar = TopStatusBar(self)
		self.add_widget(self.TopStatusBar)

		self.BottomStatusBar = BottomStatusBar(self)		
		self.add_widget(self.BottomStatusBar)

		self.LeftNavigation()
		self.Page_Welcome()
		#Sounds.PlaySound(Preload_LCARS, 'datalink.mp3')

		Preload_LCARS.PreloadEDAssets_Thread(Preload_LCARS)

	def LeftNavigation(self):
		Buttons.Button_LeftNav(self, Config_LCARS, Preload_LCARS, 'debug', 0, 2, 1, self.btn_test)
		Buttons.Button_LeftNav(self, Config_LCARS, Preload_LCARS, 'inara', 1, 2, 1, self.page_inara)
		Buttons.Button_LeftNav(self, Config_LCARS, Preload_LCARS, 'welcome', 2, 0, 1, self.welcome_page)
		Buttons.Button_LeftNav(self, Config_LCARS, Preload_LCARS, 'elite limpets', 4, 1, 1, self.elitedangerous_limpets)
		Buttons.Button_LeftNav(self, Config_LCARS, Preload_LCARS, 'elite pips', 5, 0, 1, self.elitedangerous_pips)
		Buttons.Button_LeftNav(self, Config_LCARS, Preload_LCARS, 'exit', 7, 2, 1, self.exit_page)

	Pages = ['Welcome','ElitePIPS', 'EliteLimpets', 'Exit', 'inara']

#region Pages Switches
	def welcome_page(self, instance):
		RemovesClears.clear_pages(self)
		self.Page_Welcome()
		TopStatusBar.changeCaption(self.TopStatusBar, 'Elite LCARS')
		Logger.info('PageFunction : Pageswitch - Welcome')

	def exit_page(self, instance):
		RemovesClears.clear_pages(self)
		TopStatusBar.changeCaption(self.TopStatusBar, 'shutdown')
		self.Page_Exit()
		Logger.info('PageFunction : Pageswitch - Exit')

	def exit_page1(self, instance):
		RemovesClears.remove_mywidget(self, 'Exit_auth')
		id='Exit'
		Buttons.RoundedButton(self, Config_LCARS, Preload_LCARS, id + '_auth',('btn_red_rounded_left.png', 'btn_red_rounded_right.png'), '--- CONFIRM ---', self.exit_page2, (328,81), 197, '42sp', soundFile='complete.wav')
		Logger.info('PageFunction : Pageswitch - Exit 1')

	def exit_page2(self, instance):
		RemovesClears.clear_pages(self)
		RemovesClears.remove_mywidget(self, 'Navigation')
		Clock.schedule_interval(lambda a: App.get_running_app().stop(), 4.5)

	def elitedangerous_pips(self, instance):
		RemovesClears.clear_pages(self)
		TopStatusBar.changeCaption(self.TopStatusBar, 'manage power')
		self.Page_ElitePIPS()
		Logger.info('PageFunction : Pageswitch - Elite PIPS')

	def elitedangerous_limpets(self, instance):
		RemovesClears.clear_pages(self)
		TopStatusBar.changeCaption(self.TopStatusBar, 'elite limpets')
		self.Page_EliteLimpets()
		Logger.info('PageFunction : Pageswitch - EliteLimpets')

	def page_inara(self, instance):
		RemovesClears.clear_pages(self)
		TopStatusBar.changeCaption(self.TopStatusBar, 'inara')
		self.Page_inaracz()
		Logger.info('PageFunction : Pageswitch - inara')
#endregion

#region Pages
	def initinThread(self):
		id='inaracz'
		if self.shipinstance == None:
			self.shipinstance = Ships(Config_LCARS)
		RemovesClears.remove_mywidget(self, 'inaracz')

		
		if self.shipinstance.status != None:
			status = self.shipinstance.status
		else:
			status = 'Loaded'

		lbl_info = Label(text=status, pos=(282,256), size=(325,152), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='96sp', id=id, halign='center')
		self.add_widget(lbl_info)

		

	def Page_inaracz(self):
		id='inaracz'
		lbl_info = Label(text='Loading...', pos=(282,256), size=(325,152), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='96sp', id=id, halign='center')
		self.add_widget(lbl_info)

		#threading.Thread(target=self.initinThread).start()

		#lbl_test = ScrollView(text='dasdasdsadsadsa\nfdsfdsfdsfdsfds\ndsfdsfdsfsafs33\n\n\n\nasd2d2', pos=(282,128), size=(325,152), size_hint=(None,None), id=id, font_name='fnt/lcarsgtj3.ttf', font_size='96sp')
		lbl_test = ScrollView(pos=(282,128), size=(325,152), size_hint=(None,None), id=id, bar_width=4, do_scroll_y=True, do_scroll_x=True)
		#with lbl_test.canvas.before:
		#	Color(1,0.5,0.9,1)
		#	Rectangle(pos=lbl_test.pos, size=lbl_test.size)
		
		x = Inara(Config_LCARS)
		output = None

		if x.state:
			output = 'CombatRank: ' + x.cmdr_combatrank + '\nTradeRank: ' + x.cmdr_traderank + '\n'
		else:
			output = 'Something went wrong'

		lbl_info2 = Label(text=output, pos=(0,0), size=(500,500), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='96sp', id=id, halign='center')
		lbl_test.add_widget(lbl_info2)

		self.add_widget(lbl_test)
		
	def Page_Exit(self):
		id='Exit'
		lbl_shutdown = Label(text='COMPUTER CORE\nSHUTDOWN', pos=(282,256), size=(325,152), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='96sp', id=id, halign='center')
		self.add_widget(lbl_shutdown)
		Buttons.RoundedButton(self, Config_LCARS, Preload_LCARS, id + '_auth',('btn_red_rounded_left.png', 'btn_red_rounded_right.png'), '--- AUTHORIZE ---', self.exit_page1, (239,167), 370, soundFile='beep.wav')

	def Page_Welcome(self):
		id='Welcome'
		primary = Label(text='PRIMARY SYSTEMS TERMINAL', pos=(264,339), size=(362,37), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=id)
		self.add_widget(primary)
		logo = Image(texture=Preload_LCARS.returnPreloadedAsset('logo.png'), pos=(227,182), size_hint=(None,None), size=(436,136), id=id)
		self.add_widget(logo)
		access = Label(text='ACCESS GRANTED', pos=(338,93), size=(214,38), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=id)
		self.add_widget(access)
		vid = Video(source='vid/system_prio.mp4', pos=(640,60), size_hint=(None,None), size=(140,140), id=id, state='play', volume='0', options={'allow_stretch':True, 'eos': 'loop'})
		self.add_widget(vid)

	def Page_ElitePIPS(self):
		id='ElitePIPS'

		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'engines', self.btn_speed, (118,371),233)
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'weapons', self.btn_weapons, (118,313),233)
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'system', self.btn_system, (118,256),233)
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'reset', self.btn_reset, (118,198),233)

		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'Combat turn', self.btn_combatturn, (538,340),233, backgroundColor=ColorConversion.RGBA_to_Float(None, 153,205,255), soundFile='man_combatturn.wav')
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'Alpha Strike', self.btn_alphastrike, (494,255),233, backgroundColor=ColorConversion.RGBA_to_Float(None, 181,0,6), soundFile='man_alphastrike.wav')
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'Head to Head', self.btn_headtohead, (494,170),233, backgroundColor=ColorConversion.RGBA_to_Float(None, 181,0,6), soundFile='man_headtohead.wav')
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'Omega one', self.btn_omegaone, (185,85),233, backgroundColor=ColorConversion.RGBA_to_Float(None, 0,168,89), soundFile='man_omegaone.wav')
		Buttons.RectangleButton(self, Config_LCARS, Preload_LCARS, id, 'Omega two', self.btn_omegatwo, (471,85),233, backgroundColor=ColorConversion.RGBA_to_Float(None, 0,168,89), soundFile='man_omegatwo.wav')


	def Page_EliteLimpets(self):
		id='EliteLimpets'
		btn_positions_first_row=[(124,251),(289,251),(453,251),(618,251)]
		btn_positions_second_row=[(124,49),(289,49),(453,49),(618,49)]
		#COLLECTOR
		Buttons.RoundedButtonSquare(self, Config_LCARS, Preload_LCARS, id,('btn_orange_upLeft.png','btn_orange_upRight.png','btn_orange_downLeft.png','btn_orange_downRight.png'), 'COLLECTOR', self.btn_limpets_collector, btn_positions_first_row[3], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(None, 254,154,0))
		#DECON
		Buttons.RoundedButtonSquare(self, Config_LCARS, Preload_LCARS, id,('btn_lightblue_upLeft.png','btn_lightblue_upRight.png','btn_lightblue_downLeft.png','btn_lightblue_downRight.png'), 'DECON', self.btn_limpets_decon, btn_positions_first_row[0], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(None, 153,205,255))
		#REPAIR
		Buttons.RoundedButtonSquare(self, Config_LCARS, Preload_LCARS, id,('btn_green_upLeft.png','btn_green_upRight.png','btn_green_downLeft.png','btn_green_downRight.png'), 'REPAIR', self.btn_limpets_repair, btn_positions_second_row[2], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(None, 0,168,89))

#endregion

#region Pages - Functions
	def btn_combatturn(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_alphastrike(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{RIGHT}', '{LEFT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_headtohead(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{LEFT}', '{RIGHT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_omegaone(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{LEFT}', '{LEFT}', '{UP}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_omegatwo(self, instance):
		sequence = ['{DOWN}', '{LEFT}', '{LEFT}', '{UP}', '{UP}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_reset(self, instance):
		os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key {DOWN}')

	def btn_system(self, instance):
		sequence = ['{DOWN}', '{LEFT}', '{LEFT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_weapons(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{RIGHT}', '{RIGHT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_speed(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{UP}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)

	def btn_test(self, instance):
		#print(type(returnPreloadedAsset('ringin')))
		#TopStatusBar.changeCaption(self.TopStatusBar, 'Elite LCARS')
		#RemovesClears.remove_mywidget(self, 'TopStatusBar')
		#Buttons.RoundedButtonSquare(self, Config_LCARS, Preload_LCARS, 'test',('btn_orange_upLeft.png','btn_orange_upRight.png','btn_orange_downLeft.png','btn_orange_downRight.png'), 'elite', None, (100,100), 150, 180, 'explorer_rank8', '48sp', ColorConversion.RGBA_to_Float(None, 254,154,0))
		#print(len(Preload_LCARS.preloadedAssets))

		for element in Preload_LCARS.preloadedAssets:
			if 'Federal_Dropship_schematic.png' in element[0]:
				print(element[0])
				bg = Image(texture=element[1], pos=(1,0), size_hint=(None,None), size=(800,480), id='test')
				self.add_widget(bg)

	def btn_limpets_collector(self, instance):
		sequence = ['{VK_NUMPAD4}', '{VK_NUMPAD4}', '{VK_ADD}', '{VK_NUMPAD4}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)
			time.sleep(0.1)

	def btn_limpets_decon(self, instance):
		sequence = ['{VK_NUMPAD4}', '{VK_NUMPAD0}', '{VK_NUMPAD6}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)
			time.sleep(0.1)

	def btn_limpets_repair(self, instance):
		sequence = ['{VK_NUMPAD4}', '{VK_ADD}', '{VK_NUMPAD6}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+Config_LCARS.socketfile+'" key ' + key)
			time.sleep(0.1)
#endregion

class MainApp(App):
	def build(self):
		self.title = 'LCARS'
		return MainLayout()

	def on_stop(self):
		Logger.critical('EXIT : Made with <3')

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
