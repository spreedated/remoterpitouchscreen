from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from mod.Controls import *
from mod.RemovesClears import RemovesClears

class WelcomePage(FloatLayout):
	id='Welcome'

	mainClass = None
	configClass = None
	preloadClass = None

	def __init__(self, mainClass, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass

		self.page()

	def page(self):
		primary = Label(text='PRIMARY SYSTEMS TERMINAL', pos=(264,339), size=(362,37), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=self.id)
		self.mainClass.add_widget(primary)
		logo = Image(texture=self.preloadClass.returnPreloadedAsset('logo.png'), pos=(227,182), size_hint=(None,None), size=(436,136), id=self.id)
		self.mainClass.add_widget(logo)
		access = Label(text='ACCESS GRANTED', pos=(338,93), size=(214,38), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=self.id)
		self.mainClass.add_widget(access)
		#vid = Video(source='vid/system_prio.mp4', pos=(640,60), size_hint=(None,None), size=(140,140), id=self.id, state='play', volume='0', options={'allow_stretch':True, 'eos': 'loop'})
		#self.mainClass.add_widget(vid)
