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
	os.environ['KIVY_VIDEO'] = 'null' # use for debug, no video, no warnings in console
	#os.environ['KIVY_VIDEO'] = 'gstplayer' #using kivy.deps.gstreamer
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
import configparser
import datetime
import pprint
import time
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
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from kivy.core.video import VideoBase
from kivy.uix.videoplayer import VideoPlayer

if sys.version_info[0] != 3:
	print("This script requires Python version 3.x")
	sys.exit(1)

#region CONFIG Load
config_clicksounds=1
config_socket='udp'
config_socketfile=''

confFilePath = os.getcwd() + '/config.conf'
if os.path.isfile(confFilePath):
	try:
		config = configparser.ConfigParser()
		config.read(confFilePath)
		config_socket = str(config.get('MAIN','socket'))
		config_clicksounds = int(config.get('SOUND','clicksounds'))
		Logger.info('Configuration : Loaded sucessfully')
	except Exception as e :
		print(e)
		try:
			os.remove(confFilePath)
		except Exception as e:
			print(e)
else:
	with open(confFilePath, 'x') as f:
		f.write('[MAIN]\n')
		f.write('socket=udp\n')
		f.write('\n[SOUND]\n')
		f.write('clicksounds=1\n')
		f.close()
		Logger.info('Configuration : Created successfully')

if config_socket == 'udp':
	config_socketfile = 'client_udp.py'
elif config_socket == 'tcp':
	config_socketfile = 'client_tcp.py'
#endregion

#region PreloadImages
def search_tuple(self, tups, elem):
	return filter(lambda tup: elem in tup, tups)

preloadedAssets = []
def preload_Assets():
	#preload IMAGES
	count = 0
	for file in os.listdir("img"):
		if file.endswith(".png"):
			count+=1
			preloadedAssets.append([file, Image(source='img/'+file).texture])
	if count == 1:
		Logger.info('Preload : one Imagefile loaded to memory as textures')
	else:
		Logger.info('Preload : ' + str(count) + ' Imagefiles loaded to memory as textures')
	#preload SOUNDS
	count = 0
	for r,d,f in os.walk('snd'):
		for file in os.listdir(r):
				if file.endswith(".wav") or file.endswith(".mp3"):
					count+=1
					preloadedAssets.append([os.path.join(r,file), SoundLoader.load(os.path.join(r,file))])
	if count == 1:
		Logger.info('Preload : one Soundfile loaded to memory')
	else:
		Logger.info('Preload : ' + str(count) + ' Soundfiles loaded to memory')

def returnPreloadedAsset(AssetName):
	for x in preloadedAssets:
		if AssetName in x[0]:
			return x[1]
#endregion

#region TopStatusBar
class TopStatusBar(FloatLayout):
	lbl_dot = ObjectProperty()
	lbl_time = ObjectProperty()

	def __init__(self, lblText='neXn-Systems', **kwargs):
		super().__init__(**kwargs)
		#BlackBox behind
		maincnv = Label(pos=(457,445), size=(315,25), size_hint=(None,None))
		with maincnv.canvas.before:
			Color(0,0,0,1)
			Rectangle(pos=maincnv.pos, size=maincnv.size)

		lbl_box = Label(text=lblText, pos=(459,440), size=(225,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='28sp')
		lbl_box.bind(texture_size=lbl_box.setter('size'))
		self.lbl_dot = Label(text='', pos=(690,445), size=(5,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='28sp')
		self.lbl_time = Label(text='', pos=(705,445), size=(60,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='28sp')

		self.add_widget(maincnv)
		self.add_widget(lbl_box)
		self.add_widget(self.lbl_dot)
		self.add_widget(self.lbl_time)
		self.flash(None)

	def flash(self, instance):
		Clock.schedule_interval(self.timer, 0.8)
		Clock.schedule_interval(self.timerTime, 0.1)

	def timer(self, instance):
		acc = self.lbl_dot.text
		if acc == '':
			self.lbl_dot.text = '•'
		else:
			self.lbl_dot.text = ''

	def timerTime(self, instance):
		now = datetime.datetime.now()
		self.lbl_time.text = now.strftime('%H:%M:%S')
#endregion

#region BottomStatusBar
class BottomStatusBar(FloatLayout):
	lbl_date = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#BlackBox behind
		maincnv = Label(pos=(206,10), size=(148,25), size_hint=(None,None))
		with maincnv.canvas.before:
			Color(0,0,0,1)
			Rectangle(pos=maincnv.pos, size=maincnv.size)
		self.add_widget(maincnv)

		lbl_box = Label(text='stardate:', pos=(212,8), size=(70,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='24sp')
		lbl_box.bind(texture_size=lbl_box.setter('size'))
		self.add_widget(lbl_box)

		rndint = random.randint(10000,99999)
		self.lbl_date = Label(text=str(rndint) + '.00', pos=(289,8), size=(100,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='24sp')
		self.lbl_date.bind(texture_size=self.lbl_date.setter('size'))
		self.add_widget(self.lbl_date)

		self.timerDate(None)
		Clock.schedule_interval(self.timerDate, 45)

	def timerDate(self, instance):
		rndint = random.randint(00,99)
		self.lbl_date.text = self.lbl_date.text[:self.lbl_date.text.find('.')+1] + str("{:02d}".format(rndint))
#endregion

class ColorConversion():
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		return

	def RGBA_to_Float(self, R, G, B, A=255):
		R = float("{0:.2f}".format(R/255))
		G = float("{0:.2f}".format(G/255))
		B = float("{0:.2f}".format(B/255))
		A = float("{0:.2f}".format(A/255))

		return (R,G,B,A)

class MyButton(ButtonBehavior, Label):
	def on_press(self):
		pass

class MyImageButton(ButtonBehavior, Image):
	def on_press(self):
		pass

class MainLayout(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		bg = Image(texture=returnPreloadedAsset('bg.png'), pos=(1,0), size_hint=(None,None), size=(800,480), id='background')
		self.add_widget(bg)
		txt_menu = Label(text='MENU', pos=(42,435), size=(35,18), size_hint=(None,None), color=(0,0,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28 sp')
		self.add_widget(txt_menu)

		self.add_widget(TopStatusBar())
		self.add_widget(BottomStatusBar())
		self.LeftNavigation()
		self.Page_Welcome()
		self.PlaySound('datalink.mp3')

	def LeftNavigation(self):
		self.ButtonCreation_LeftNavigation('welcome', 2, 0, 1, 2)
		self.ButtonCreation_LeftNavigation('debug', 1, 2, 1, 3)
		self.ButtonCreation_LeftNavigation('elite limpets', 4, 1, 1, 4)
		self.ButtonCreation_LeftNavigation('elite pips', 5, 0, 1, 1)
		self.ButtonCreation_LeftNavigation('exit', 7, 2, 1, 0)

	def EnumFunctions(self, instance, enum):
		if enum == 0:
			return self.exit_page
		if enum == 1:
			return self.elitedangerous_pips
		if enum == 2:
			return self.welcome_page
		if enum == 3:
			return self.btn_test
		if enum == 4:
			return self.elitedangerous_limpets

#region Removes&Clears
	def clear_pages(self):
		for x in range(8):
			for child in self.children:
				if child.id != None:
					for page in self.Pages:
						if page in child.id:
							if type(child) == Video:
								child.unload()
							if type(child) == VideoPlayer:
								child.state = 'stop'
							self.remove_widget(child)
		Logger.info('PageFunction : Pages cleared')

	def remove_mywidget(self, widget_id):
		for x in range(5):
			for child in self.children:
				if child.id != None:
					if widget_id in child.id:
						self.remove_widget(child)
#endregion

	def EnumPosition(self, instance, enum):
		if enum == 0:
			return (11,383)
		if enum == 1:
			return (11,336)
		if enum == 2:
			return (11,290)
		if enum == 3:
			return (11,243)
		if enum == 4:
			return (11,196)
		if enum == 5:
			return (11,150)
		if enum == 6:
			return (11,103)
		if enum == 7:
			return (11,56)

#region Buttons
	def ButtonCreation_LeftNavigation(self, btnText, btnEnumPosition, btnEnumColor, btnClickSounds=0, btnEnumFunction=None):
		btn = MyButton(pos=self.EnumPosition(self, btnEnumPosition), size=(96,40), size_hint=(None,None), id='btnLeftNavigation')
		with btn.canvas.before:
			if btnEnumColor == 0: #Yellow
				Color(1,1,0.2,1)
			if btnEnumColor == 1: #Light yellow
				Color(0.95,0.99,0.44,1)
			if btnEnumColor == 2: #Blue
				Color(0.6,0.8,1,1)
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=btnText, pos=(btn.pos[0]+2,btn.pos[1]-5), size=(50,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), id='btnLeftNavigation')
		btn_txt.bind(texture_size=btn_txt.setter('size'))

		elements = [btn,btn_txt]
		for x in elements:
			x.bind(on_press=self.EnumFunctions(self, btnEnumFunction))
			if config_clicksounds == 1:
				x.bind(on_press=self.PlayClickSound)
			self.add_widget(x)

	def RoundedButton(self, id, images, labeltext, action, position, width, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(1,1,1,1), clickSound=True, soundFile=None):
		btn_left = MyImageButton(texture=returnPreloadedAsset(images[0]), pos=position, size_hint=(None,None), size=(23,46), id=id)
		btn_right = MyImageButton(texture=returnPreloadedAsset(images[1]), pos=(position[0]+19+width, position[1]), size_hint=(None,None), size=(23,46), id=id)
		btn_center = MyButton(pos=(position[0]+21,position[1]+1), size=(width,45), size_hint=(None,None), id=id)
		with btn_center.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_center.pos, size=btn_center.size)
		btn_lbl = MyButton(text=labeltext, pos=(position[0]+21,position[1]+7), size=(width,31), size_hint=(None,None), color=(foregroundColor[0],foregroundColor[1],foregroundColor[2],foregroundColor[3]), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, id=id, halign='center')

		elements = [btn_right,btn_left,btn_center,btn_lbl]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and config_clicksounds == 1 and soundFile == None:
				x.bind(on_press=self.PlayClickSound)
			if soundFile != None:
				x.bind(on_press=lambda a:self.PlaySound(soundFile))
			self.add_widget(x)

	def RoundedButtonSquare(self, id, cornerImages, labeltext, action, position, width, height, iconImage, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		width = width-64
		height = height-32
		btn_upLeft = MyImageButton(texture=returnPreloadedAsset(cornerImages[0]), pos=(position[0],position[1]+height), size_hint=(None,None), size=(32,32), id=id)
		btn_upRight = MyImageButton(texture=returnPreloadedAsset(cornerImages[1]), pos=(position[0]+width+33,position[1]+height), size_hint=(None,None), size=(32,32), id=id)
		btn_downLeft = MyImageButton(texture=returnPreloadedAsset(cornerImages[2]), pos=(position[0],position[1]), size_hint=(None,None), size=(32,32), id=id)
		btn_downRight = MyImageButton(texture=returnPreloadedAsset(cornerImages[3]), pos=(position[0]+width+33,position[1]-1), size_hint=(None,None), size=(32,32), id=id)

		btn_upCenter = MyButton(pos=(position[0]+32,position[1]+height), size=(width+2,32), size_hint=(None,None), id=id)
		with btn_upCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_upCenter.pos, size=btn_upCenter.size)
		btn_downCenter = MyButton(pos=(position[0]+32,position[1]), size=(width+2,32), size_hint=(None,None), id=id)
		with btn_downCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_downCenter.pos, size=btn_downCenter.size)

		btn_leftCenter = MyButton(pos=(position[0],position[1]+31), size=(32,(height-31)), size_hint=(None,None), id=id)
		with btn_leftCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_leftCenter.pos, size=btn_leftCenter.size)
		btn_rightCenter = MyButton(pos=(position[0]+width+32,position[1]+30), size=(32,(height-30)), size_hint=(None,None), id=id)
		with btn_rightCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_rightCenter.pos, size=btn_rightCenter.size)

		btn_Center = MyButton(pos=(position[0]+32,position[1]+32), size=(width,(height-32)), size_hint=(None,None), id=id)
		with btn_Center.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_Center.pos, size=btn_Center.size)

		btn_lbl = MyButton(text=labeltext, pos=(position[0],position[1]+12), size=(width+64,32), size_hint=(None,None), color=(foregroundColor[0],foregroundColor[1],foregroundColor[2],foregroundColor[3]), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, id=id, halign='center')

		btn_icon = MyImageButton(texture=returnPreloadedAsset(iconImage), pos=(position[0]+((width+64)/2),position[1]+(((height+32)/100)*30)), size=(width+(((width+64)/100)*15), height-(((height+32)/100)*15)), size_hint=(None,None), id=id)
		btn_icon.pos=(btn_icon.pos[0]-(btn_icon.size[0]/2),btn_icon.pos[1])

		elements = [btn_downRight,btn_downLeft,btn_upLeft,btn_upRight,btn_Center,btn_rightCenter,btn_leftCenter,btn_downCenter,btn_upCenter,btn_lbl,btn_icon]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and config_clicksounds == 1 and soundFile == None:
				x.bind(on_press=self.PlayClickSound)
			if soundFile != None:
				x.bind(on_press=lambda a:self.PlaySound(soundFile))
			self.add_widget(x)

	def RectangleButton(self, id, labeltext, action, position, width, iconImage=None, textsize='36sp', backgroundColor=(1,1,0,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		btn = MyButton(pos=(position[0],position[1]), size=(width,46), size_hint=(None,None), id=id)
		with btn.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=labeltext, pos=(position[0],position[1]), size=(width,44), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size=textsize, color=foregroundColor, markup=True, id=id, halign='center')

		elements = [btn, btn_txt]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and config_clicksounds == 1 and soundFile == None:
				x.bind(on_press=self.PlayClickSound)
			if soundFile != None:
				x.bind(on_press=lambda a:self.PlaySound(soundFile))
			self.add_widget(x)

#endregion

	Pages = ['Welcome','ElitePIPS', 'EliteLimpets', 'Exit']
#region Pages Switches
	def welcome_page(self, instance):
		self.clear_pages()
		self.Page_Welcome()
		Logger.info('PageFunction : Pageswitch - Welcome')

	def exit_page(self, instance):
		self.clear_pages()
		self.Page_Exit()
		Logger.info('PageFunction : Pageswitch - Exit')

	def exit_page1(self, instance):
		self.remove_mywidget('Exit_auth')
		id='Exit'
		self.RoundedButton(id + '_auth',('btn_red_rounded_left.png', 'btn_red_rounded_right.png'), '--- CONFIRM ---', self.exit_page2, (328,81), 197, '42sp', soundFile='complete.wav')
		Logger.info('PageFunction : Pageswitch - Exit 1')

	def exit_page2(self, instance):
		self.clear_pages()
		self.remove_mywidget('Navigation')
		Clock.schedule_interval(lambda a: App.get_running_app().stop(), 4.5)

	def elitedangerous_pips(self, instance):
		self.clear_pages()
		self.Page_ElitePIPS()
		Logger.info('PageFunction : Pageswitch - Elite PIPS')

	def elitedangerous_limpets(self, instance):
		self.clear_pages()
		self.Page_EliteLimpets()
		Logger.info('PageFunction : Pageswitch - EliteLimpets')
#endregion

#region Pages
	def Page_Exit(self):
		id='Exit'
		lbl_shutdown = Label(text='COMPUTER CORE\nSHUTDOWN', pos=(282,256), size=(325,152), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='96sp', id=id, halign='center')
		self.add_widget(lbl_shutdown)
		self.RoundedButton(id + '_auth',('btn_red_rounded_left.png', 'btn_red_rounded_right.png'), '--- AUTHORIZE ---', self.exit_page1, (239,167), 370, soundFile='beep.wav')

	def Page_Welcome(self):
		id='Welcome'
		primary = Label(text='PRIMARY SYSTEMS TERMINAL', pos=(264,339), size=(362,37), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=id)
		self.add_widget(primary)
		logo = Image(texture=returnPreloadedAsset('logo.png'), pos=(227,182), size_hint=(None,None), size=(436,136), id=id)
		self.add_widget(logo)
		access = Label(text='ACCESS GRANTED', pos=(338,93), size=(214,38), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=id)
		self.add_widget(access)
		vid = Video(source='vid/system_prio.mp4', pos=(640,60), size_hint=(None,None), size=(140,140), id=id, state='play', volume='0', options={'allow_stretch':True, 'eos': 'loop'})
		self.add_widget(vid)

	def Page_ElitePIPS(self):
		id='ElitePIPS'
		
		self.RectangleButton(id, 'engines', self.btn_speed, (328,319),233)
		self.RectangleButton(id, 'weapons', self.btn_weapons, (511,211),233)
		self.RectangleButton(id, 'reset', self.btn_reset, (328,117),233)
		self.RectangleButton(id, 'system', self.btn_system, (142,211),233)


	def Page_EliteLimpets(self):
		id='EliteLimpets'
		btn_positions_first_row=[(124,251),(289,251),(453,251),(618,251)]
		btn_positions_second_row=[(124,49),(289,49),(453,49),(618,49)]
		#COLLECTOR
		self.RoundedButtonSquare(id,('btn_orange_upLeft.png','btn_orange_upRight.png','btn_orange_downLeft.png','btn_orange_downRight.png'), 'COLLECTOR', self.btn_limpets_collector, btn_positions_first_row[3], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(None, 254,154,0))
		#DECON
		self.RoundedButtonSquare(id,('btn_lightblue_upLeft.png','btn_lightblue_upRight.png','btn_lightblue_downLeft.png','btn_lightblue_downRight.png'), 'DECON', self.btn_limpets_decon, btn_positions_first_row[0], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(None, 153,205,255))
		#REPAIR
		self.RoundedButtonSquare(id,('btn_green_upLeft.png','btn_green_upRight.png','btn_green_downLeft.png','btn_green_downRight.png'), 'REPAIR', self.btn_limpets_repair, btn_positions_second_row[2], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(None, 0,168,89))

#endregion

#region Pages - Functions
	def btn_reset(self, instance):
		os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key {DOWN}')

	def btn_system(self, instance):
		sequence = ['{DOWN}', '{LEFT}', '{LEFT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key ' + key)

	def btn_weapons(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{RIGHT}', '{RIGHT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key ' + key)

	def btn_speed(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{UP}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key ' + key)

	def btn_test(self, instance):
		print(type(returnPreloadedAsset('ringin')))

	def btn_limpets_collector(self, instance):
		sequence = ['{VK_NUMPAD4}', '{VK_NUMPAD4}', '{VK_ADD}', '{VK_NUMPAD4}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key ' + key)
			time.sleep(0.1)

	def btn_limpets_decon(self, instance):
		sequence = ['{VK_NUMPAD4}', '{VK_NUMPAD0}', '{VK_NUMPAD6}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key ' + key)
			time.sleep(0.1)

	def btn_limpets_repair(self, instance):
		sequence = ['{VK_NUMPAD4}', '{VK_ADD}', '{VK_NUMPAD6}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+config_socketfile+'" key ' + key)
			time.sleep(0.1)
#endregion

#region Sounds
	#Play RandomSound
	def PlayRndSound(self, instance):
		rndlist = []
		count = 0
		for x in preloadedAssets:
			if 'clicks' in x[0]:
				count+=1
				rndlist.append(x[0])
		rndint = random.randint(0,count-1)
		returnPreloadedAsset(rndlist[rndint]).play()

	def PlayClickSound(self, instance):
		x = returnPreloadedAsset('207.wav')
		if x != None:
			x.seek(0)
			x.play()
		else:
			Logger.error('Sound : File 404')

	def PlaySound(self, soundFileName):
		x = returnPreloadedAsset(soundFileName)
		if x != None:
			x.seek(0)
			x.play()
		else:
			Logger.error('Sound : File 404')

#endregion

class MainApp(App):
	def build(self):
		self.title = 'LCARS'
		preload_Assets()
		return MainLayout()

	def on_stop(self):
		Logger.critical('EXIT : Made with <3')

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
