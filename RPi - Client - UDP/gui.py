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
clicksounds=1

confFilePath = os.getcwd() + '/config.conf'
if os.path.isfile(confFilePath):
	try:
		config = configparser.ConfigParser()
		config.read(confFilePath)
		clicksounds = int(config.get('MAIN','clicksounds'))
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

class UpperRightIndicator(FloatLayout):
	lbl_dot = ObjectProperty()
	lbl_time = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#BlackBox behind
		maincnv = Label(pos=(457,445), size=(315,25), size_hint=(None,None))
		with maincnv.canvas.before:
			Color(0,0,0,1)
			Rectangle(pos=maincnv.pos, size=maincnv.size)

		lbl_box = Label(text='neXn-Systems', pos=(460,445), size=(120,25), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28sp')
		self.lbl_dot = Label(text='', pos=(690,445), size=(5,25), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28sp')
		self.lbl_time = Label(text='', pos=(705,445), size=(60,25), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28sp')

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

class MyButton(ButtonBehavior, Label):
	def on_press(self):
		if clicksounds:
			self.PlayRndSound()

	#Play RandomSound
	def PlayRndSound(self):
		sounds = []
		for sndfile in os.listdir('snd/clicks/'):
			sounds.append('snd/clicks/' + str(sndfile))
		rndint = random.randint(0,len(sounds)-1)
		sound = SoundLoader.load(sounds[rndint])
		sound.play()

class Navigation(RelativeLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#button0
		btn0 = MyButton(pos=(11,383), size=(96,40), size_hint=(None,None))
		with btn0.canvas.before:
			Color(1,1,0.2,1)
			Rectangle(pos=btn0.pos, size=btn0.size)
		btn0_txt = Label(text='[b]CONFIGURE[/b]', pos=(btn0.pos[0]+4,btn0.pos[1]+2), size=(50,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		self.add_widget(btn0)
		self.add_widget(btn0_txt)

		#button1
		btn1 = MyButton(pos=(11,336), size=(96,40), size_hint=(None,None))
		with btn1.canvas.before:
			Color(0.6,0.8,1,1)
			Rectangle(pos=btn1.pos, size=btn1.size)
		btn1_txt = Label(text='[b]OPTIONS[/b]', pos=(btn1.pos[0]+4,btn1.pos[1]+2), size=(40,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		self.add_widget(btn1)
		self.add_widget(btn1_txt)

		#button2
		btn2 = MyButton(pos=(11,290), size=(96,40), size_hint=(None,None))
		with btn2.canvas.before:
			Color(0.6,0.8,1,1)
			Rectangle(pos=btn2.pos, size=btn2.size)
		btn2_txt = Label(text='[b]OPTIONS[/b]', pos=(btn2.pos[0]+4,btn2.pos[1]+2), size=(40,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		self.add_widget(btn2)
		self.add_widget(btn2_txt)

		#button3
		btn3 = MyButton(pos=(11,243), size=(96,40), size_hint=(None,None))
		with btn3.canvas.before:
			Color(0.6,0.8,1,1)
			Rectangle(pos=btn3.pos, size=btn3.size)
		btn3_txt = Label(text='[b]OPTIONS[/b]', pos=(btn3.pos[0]+4,btn3.pos[1]+2), size=(40,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		self.add_widget(btn3)
		self.add_widget(btn3_txt)

		#button4
		btn4 = MyButton(pos=(11,196), size=(96,40), size_hint=(None,None))
		with btn4.canvas.before:
			Color(0.6,0.8,1,1)
			Rectangle(pos=btn4.pos, size=btn4.size)
		btn4_txt = Label(text='[b]OPTIONS[/b]', pos=(btn4.pos[0]+4,btn4.pos[1]+2), size=(40,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		self.add_widget(btn4)
		self.add_widget(btn4_txt)

		#button5
		btn5 = MyButton(pos=(11,150), size=(96,40), size_hint=(None,None))
		with btn5.canvas.before:
			Color(0.6,0.8,1,1)
			Rectangle(pos=btn5.pos, size=btn5.size)
		btn5_txt = Label(text='[b]OPTIONS[/b]', pos=(btn5.pos[0]+4,btn5.pos[1]+2), size=(40,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		self.add_widget(btn5)
		self.add_widget(btn5_txt)

		#button6
		btn6 = MyButton(pos=(11,103), size=(96,40), size_hint=(None,None))
		with btn6.canvas.before:
			Color(0.6,0.8,1,1)
			Rectangle(pos=btn6.pos, size=btn6.size)
		btn6_txt = Label(text='[b]Elite[/b]', pos=(btn6.pos[0]+4,btn6.pos[1]+2), size=(40,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)

		btn6.bind(on_press=self.elitedangerous)
		self.add_widget(btn6)
		self.add_widget(btn6_txt)

		#button7
		btn7 = MyButton(pos=(11,56), size=(96,40), size_hint=(None,None))
		with btn7.canvas.before:
			Color(1,1,0.2,1)
			Rectangle(pos=btn7.pos, size=btn7.size)
		btn7_txt = Label(text='[b]EXIT[/b]', pos=(btn7.pos[0]+4,btn7.pos[1]+2), size=(20,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='22sp', color=(0,0,0,1), markup=True)
		btn7.bind(on_press=self.exitapp)
		self.add_widget(btn7)
		self.add_widget(btn7_txt)

	def exitapp(self, instance):
		App.get_running_app().stop()

	def elitedangerous(self, instance):
		#MainLayout.remove(MainLayout)
		#self.add_widget(ContentGrid_EliteDangerous())
		app = App.get_running_app()
		print(app.ids)

class ContentGrid_WelcomeScreen(FloatLayout):
	def __init__(self, **kwargs):
		super(ContentGrid_WelcomeScreen, self).__init__(**kwargs)
		primary = Label(text='PRIMARY SYSTEMS TERMINAL', pos=(264,339), size=(362,37), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp')
		self.add_widget(primary)
		logo = Image(source='img/logo.png', pos=(227,182), size_hint=(None,None), size=(436,136))
		self.add_widget(logo)
		access = Label(text='ACCESS GRANTED', pos=(338,93), size=(214,38), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp')
		self.add_widget(access)

class ContentGrid_EliteDangerous(FloatLayout):
	def __init__(self, **kwargs):
		super(ContentGrid_EliteDangerous, self).__init__(**kwargs)

		#button reset
		btn0 = MyButton(pos=(328,117), size=(233,46), size_hint=(None,None))
		with btn0.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn0.pos, size=btn0.size)
		btn0_txt = Label(text='[b]RESET[/b]', pos=(328,117), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True)

		btn0.bind(on_press=self.btn_reset)
		btn0_txt.bind(on_press=self.btn_reset)

		self.add_widget(btn0)
		self.add_widget(btn0_txt)

		#button SYSTEM
		btn_system = MyButton(pos=(142,216), size=(233,46), size_hint=(None,None))
		with btn_system.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn_system.pos, size=btn_system.size)
		btn_system_txt = Label(text='[b]SYSTEM[/b]', pos=(142,216), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True)

		btn_system.bind(on_press=self.btn_system)
		btn_system_txt.bind(on_press=self.btn_system)

		self.add_widget(btn_system)
		self.add_widget(btn_system_txt)

		#button WEAPONS
		btn_weapons = MyButton(pos=(511,221), size=(233,46), size_hint=(None,None))
		with btn_weapons.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn_weapons.pos, size=btn_weapons.size)
		btn_weapons_txt = Label(text='[b]WEAPONS[/b]', pos=(511,221), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True)

		btn_weapons.bind(on_press=self.btn_weapons)
		btn_weapons_txt.bind(on_press=self.btn_weapons)

		self.add_widget(btn_weapons)
		self.add_widget(btn_weapons_txt)

		#button speed
		btn_speed = MyButton(pos=(328,319), size=(233,46), size_hint=(None,None))
		with btn_speed.canvas.before:
			Color(1,1,0,1)
			Rectangle(pos=btn_speed.pos, size=btn_speed.size)
		btn_speed_txt = Label(text='[b]Speed[/b]', pos=(328,319), size=(233,46), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), markup=True)

		btn_speed.bind(on_press=self.btn_speed)
		btn_speed_txt.bind(on_press=self.btn_speed)

		self.add_widget(btn_speed)
		self.add_widget(btn_speed_txt)

	def btn_reset(self, instance):
		os.system('python "' + os.getcwd() + '/client_rpi.py" key down')

	def btn_system(self, instance):
		os.system('python "' + os.getcwd() + '/client_rpi.py" key down')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key left')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key left')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key left')

	def btn_weapons(self, instance):
		os.system('python "' + os.getcwd() + '/client_rpi.py" key down')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key right')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key right')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key right')

	def btn_speed(self, instance):
		os.system('python "' + os.getcwd() + '/client_rpi.py" key down')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key up')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key up')
		os.system('python "' + os.getcwd() + '/client_rpi.py" key up')

class MainLayout(FloatLayout):
	bg = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.bg = Image(source='img/bg.png', pos=(1,0), size_hint=(None,None), size=(800,480), id='background')
		self.add_widget(self.bg)
		txt_menu = Label(text='MENU', pos=(42,435), size=(35,18), size_hint=(None,None), color=(0,0,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28 sp')
		self.add_widget(txt_menu)

		self.add_widget(Navigation())
		self.add_widget(UpperRightIndicator())
		#self.add_widget(ContentGrid_WelcomeScreen())
		self.add_widget(ContentGrid_EliteDangerous())

	def remove(self):
		self.remove_widget(self.bg)

class MainApp(App):
	def build(self):
		self.title = 'LCARS'
		return MainLayout()

	def on_stop(self):
		Logger.critical('Good Bye')

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
