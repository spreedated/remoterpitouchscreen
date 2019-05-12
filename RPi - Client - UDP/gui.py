#!/usr/bin/python
import os
#os.environ['KIVY_GL_BACKEND'] = 'gl'
import sys
import random
import configparser
import datetime
import pprint
from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.config import Config
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

#Init Conffile
config_clicksounds=1

confFilePath = os.getcwd() + '/config.conf'
if os.path.isfile(confFilePath):
	try:
		config = configparser.ConfigParser()
		config.read(confFilePath)
		config_clicksounds = int(config.get('MAIN','clicksounds'))
		print('[+] conf loaded success...')
	except Exception as e :
		print(e)
		try:
			os.remove(confFilePath)
		except Exception as e:
			print(e)
else:
	with open(confFilePath, 'x') as f:
		f.write('[MAIN]\n')
		f.write('clicksounds=1\n')
		f.close()

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

class MainLayout(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		bg = Image(source='img/bg.png', pos=(1,0), size_hint=(None,None), size=(800,480), id='background')
		self.add_widget(bg)
		txt_menu = Label(text='MENU', pos=(42,435), size=(35,18), size_hint=(None,None), color=(0,0,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28 sp')
		self.add_widget(txt_menu)

		self.add_widget(TopStatusBar())
		self.add_widget(BottomStatusBar())
		self.LeftNavigation()
		self.Page_Welcome()

	def LeftNavigation(self):
		self.ButtonCreation_LeftNavigation('welcome', 2, 0, 1, 2)
		self.ButtonCreation_LeftNavigation('elite pips', 5, 1, 0, 1)
		self.ButtonCreation_LeftNavigation('exit', 7, 2, 1, 0)

	def EnumFunctions(self, instance, enum):
		if enum == 0:
			return self.exitapp
		if enum == 1:
			return self.elitedangerous_pips
		if enum == 2:
			return self.welcome_page

	Pages = ['Welcome','ElitePIPS']

	def clear_pages(self):
		for x in range(5):
			for child in self.children:
				if child.id != None:
					for page in self.Pages:
						if page in child.id:
							self.remove_widget(child)
		Logger.info('PageFunction : Pages cleared')

	def welcome_page(self, instance):
		self.clear_pages()
		self.Page_Welcome()
		Logger.info('PageFunction : Pageswitch - Welcome')

	def elitedangerous_pips(self, instance):
		self.clear_pages()
		self.Page_ElitePIPS()
		Logger.info('PageFunction : Pageswitch - Elite PIPS')

	def exitapp(self, instance):
		Clock.schedule_interval(lambda a: App.get_running_app().stop(), 0.5)

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

	def ButtonCreation_LeftNavigation(self, btnText, btnEnumPosition, btnEnumColor, btnClickSounds=0, btnEnumFunction=None):
		btn = MyButton(pos=self.EnumPosition(self, btnEnumPosition), size=(96,40), size_hint=(None,None))
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

		if btnClickSounds != 0 and config_clicksounds != 0:
			btn.bind(on_press=self.PlayRndSound)
			btn_txt.bind(on_press=self.PlayRndSound)

		if btnEnumFunction != None:
			btn.bind(on_press=self.EnumFunctions(self, btnEnumFunction))
			btn_txt.bind(on_press=self.EnumFunctions(self, btnEnumFunction))

		self.add_widget(btn)
		self.add_widget(btn_txt)

#region Sounds
	#Play RandomSound
	SoundPool_firstRun = True
	SoundPool_Clicks = []
	def fill_pool(self):
		if self.SoundPool_firstRun == True:
			for sndfile in os.listdir('snd/clicks/'):
				self.SoundPool_Clicks.append('snd/clicks/' + str(sndfile))
			self.SoundPool_firstRun = False
			Logger.info('Sound Function : Initialized pool')

	def PlayRndSound(self, instance):
		rndint = random.randint(0,len(self.SoundPool_Clicks)-1)
		sound = SoundLoader.load(self.SoundPool_Clicks[rndint])
		sound.play()

#endregion

	def Page_Welcome(self):
		id='Welcome'
		primary = Label(text='PRIMARY SYSTEMS TERMINAL', pos=(264,339), size=(362,37), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=id)
		self.add_widget(primary)
		logo = Image(source='img/logo.png', pos=(227,182), size_hint=(None,None), size=(436,136), id=id)
		self.add_widget(logo)
		access = Label(text='ACCESS GRANTED', pos=(338,93), size=(214,38), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=id)
		self.add_widget(access)
		#Init Functions
		self.fill_pool()

	def Page_ElitePIPS(self):
		id='ElitePIPS'
		#button reset
		btn0 = MyButton(pos=(328,117), size=(233,46), size_hint=(None,None), id=id)
		with btn0.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn0.pos, size=btn0.size)
		btn0_txt = Label(text='[b]RESET[/b]', pos=(328,117), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True, id=id)

		btn0.bind(on_press=self.btn_reset)
		btn0_txt.bind(on_press=self.btn_reset)

		self.add_widget(btn0)
		self.add_widget(btn0_txt)

		#button SYSTEM
		btn_system = MyButton(pos=(142,216), size=(233,46), size_hint=(None,None), id=id)
		with btn_system.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn_system.pos, size=btn_system.size)
		btn_system_txt = Label(text='[b]SYSTEM[/b]', pos=(142,216), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True, id=id)

		btn_system.bind(on_press=self.btn_system)
		btn_system_txt.bind(on_press=self.btn_system)

		self.add_widget(btn_system)
		self.add_widget(btn_system_txt)

		#button WEAPONS
		btn_weapons = MyButton(pos=(511,221), size=(233,46), size_hint=(None,None), id=id)
		with btn_weapons.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn_weapons.pos, size=btn_weapons.size)
		btn_weapons_txt = Label(text='[b]WEAPONS[/b]', pos=(511,221), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True, id=id)

		btn_weapons.bind(on_press=self.btn_weapons)
		btn_weapons_txt.bind(on_press=self.btn_weapons)

		self.add_widget(btn_weapons)
		self.add_widget(btn_weapons_txt)

		#button speed
		btn_speed = MyButton(pos=(328,319), size=(233,46), size_hint=(None,None), id=id)
		with btn_speed.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn_speed.pos, size=btn_speed.size)
		btn_speed_txt = Label(text='[b]Speed[/b]', pos=(328,319), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True, id=id)

		btn_speed.bind(on_press=self.btn_speed)
		btn_speed_txt.bind(on_press=self.btn_speed)

		self.add_widget(btn_speed)
		self.add_widget(btn_speed_txt)

	def btn_reset(self, instance):
		os.system('python "' + os.getcwd() + '/client_rpi.py" key {DOWN}')

	def btn_system(self, instance):
		sequence = ['{DOWN}', '{LEFT}', '{LEFT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/client_rpi.py" key ' + key)

	def btn_weapons(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{RIGHT}', '{RIGHT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/client_rpi.py" key ' + key)

	def btn_speed(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{UP}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/client_rpi.py" key ' + key)

class MainApp(App):
	def build(self):
		self.title = 'LCARS'
		return MainLayout()

	def on_stop(self):
		Logger.critical('EXIT : Made with <3')

if __name__ == '__main__':
	#Window.show_cursor = False
	#Window.borderless = True
	Window.size = (800, 480)
	# Config.set('graphics', 'fullscreen', 'false')
	# Config.set('graphics', 'window_state', 'normal')
	Config.set('graphics', 'resizable', False)
	Config.set('kivy','window_icon','ico/icon.ico')
	Config.set('kivy', 'show_fps', 1)
	Config.write()
	MainApp().run()
