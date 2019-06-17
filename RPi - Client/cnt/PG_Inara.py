import datetime
import time
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.logger import Logger
from mod.Color import ColorConversion, Colors
from mod.API_Works import API_Inara
from mod.Controls import *
from mod.Sound import Sounds
from mod.RemovesClears import RemovesClears
from cnt.PG_Inara_Fleet import *
from cnt.PG_Inara_Components import *

Builder.load_string("""
<PG_Inara>:
	Label:
		pos: 118,371
		size: 78,60
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col1
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 118,49
		size: 78,30
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col2
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 415,250
		size: 26,13
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col3
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 415,231
		size: 26,13
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col3
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 623,250
		size: 114,13
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col3
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 623,231
		size: 114,13
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col3
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 744,250
		size: 26,13
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col4
			Rectangle:
				pos: self.pos
				size: self.size
	Label:
		pos: 744,231
		size: 26,13
		size_hint: None,None
		canvas.before:
			Color:
				rgba: root.col4
			Rectangle:
				pos: self.pos
				size: self.size
	Image:
		pos: 118,81
		size: 501,287
		size_hint: None,None
		id: background
""")

class PG_Inara(FloatLayout):
	id='inaracz'

	mainClass = None
	configClass = None
	preloadClass = None
	infoClass = None

	hexagon = Image()
	hexagon_timer =  None

	col1 = ColorConversion.RGBA_to_Float(156,160,255)
	col2 = ColorConversion.RGBA_to_Float(0,168,89)
	col3 = ColorConversion.RGBA_to_Float(255,94,45)
	col4 = ColorConversion.RGBA_to_Float(181,0,6)

	def __init__(self, mainClass, configClass, preloadClass, infoClass, **kwargs):
		super().__init__(**kwargs)
		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass
		self.infoClass = infoClass

		self.ids['background'].texture = preloadClass.returnPreloadedAsset('bg_inara.png')
		self.hexagon.texture = preloadClass.returnPreloadedAsset('inara_hexagon.png')

		#animation
		self.hexagon = Image(texture=self.preloadClass.returnPreloadedAsset('inara_hexagon.png'), pos=(465,236), size_hint=(None,None), size=(40,23), id=self.id + '_hexagon')
		self.mainClass.add_widget(self.hexagon)

		self.animation()
		# ###

		#DEBUG
		#if len(self.configClass.inara_username) >= 3 and len(self.configClass.inara_password) >= 3:
		#	Buttons.Inara_MainButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'fleet', (212,155), lambda a: self.Goto_ChildPage('fleet'), foregroundColor=ColorConversion.RGBA_to_Float(0,0,0))
		#	Buttons.Inara_MainButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'components', (515,155), lambda a: self.Goto_ChildPage('components'), foregroundColor=ColorConversion.RGBA_to_Float(0,0,0))
		#return

		if self.infoClass.cmdr_name == None and self.infoClass.cmdr_combatrank == None:
			#Loading up INARA API Works
			lbl_info = Label(text='Loading...', pos=(204,288), size=(577,120), size_hint=(None,None), color=Colors.standardFont, markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=self.id, halign='center')
			self.add_widget(lbl_info)
		
			x = API_Inara(self.configClass, self.infoClass)
			output = None

			if x.errormsg != None:
				lbl_info.text = x.errormsg
				return # Stop here if something went wrong, like wrong api key
		
			Sounds.PlaySound(self.preloadClass, self.configClass, 'establishing_datalink.wav')
			self.remove_widget(lbl_info)
			# ###
		elif self.configClass.debug:
			Logger.info('Page_Inara : Information already retrieved, using old')

		#Add Rankings Combat Icons and Labels
		Buttons.Inara_RankButton(self, self.configClass, self.preloadClass, self.id, 'combat', self.infoClass.cmdr_combatrank, (200,279), ColorConversion.RGBA_to_Float(181,0,6))
		Buttons.Inara_RankButton(self, self.configClass, self.preloadClass, self.id, 'trade', self.infoClass.cmdr_traderank, (348,279), ColorConversion.RGBA_to_Float(254,154,0))
		Buttons.Inara_RankButton(self, self.configClass, self.preloadClass, self.id, 'exploration', self.infoClass.cmdr_explorationrank, (495,279), ColorConversion.RGBA_to_Float(153,205,255))
		Buttons.Inara_RankButton(self, self.configClass, self.preloadClass, self.id, 'cqc', self.infoClass.cmdr_cqcrank, (642,279), ColorConversion.RGBA_to_Float(237,26,33))

		#Buttons
		if len(self.configClass.inara_username) >= 3 and len(self.configClass.inara_password) >= 3:
			Buttons.Inara_MainButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'fleet', (212,155), lambda a: self.Goto_ChildPage('fleet'), foregroundColor=Colors.black)
			Buttons.Inara_MainButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'components', (515,155), lambda a: self.Goto_ChildPage('components'), foregroundColor=Colors.black)

	def animation(self):
		self.hexagon_timer = Clock.schedule_interval(lambda a: self.timer(), 0.02)

	direction = 'r'
	def timer(self):
		#kill timer if page not active
		active = False
		for x in range(5):
			for child in self.mainClass.children:
				if child.id != None:
					if 'hexagon' in child.id:
						active = True

		if active == False:
			self.hexagon_timer.cancel()
			if self.configClass.debug:
				Logger.info('Page_Inara : Animation timer stopped')
		# ###

		acc = self.hexagon.pos

		if self.direction == 'r':
			self.hexagon.pos = (acc[0]+1,acc[1])
			if acc[0] >= 517:
				self.direction = 'l'
		else:
			self.hexagon.pos = (acc[0]-1,acc[1])
			if acc[0] <= 465:
				self.direction = 'r'

	def Goto_ChildPage(self, page):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		if page == 'fleet':
			self.mainClass.add_widget(PG_Inara_Fleet(self.configClass, self.preloadClass, self.infoClass))
		if page == 'components':
			self.mainClass.add_widget(PG_Inara_Components(self.configClass, self.preloadClass, self.infoClass))

	def Goto_Back_MainWindow(self):
		self.Page_Main()
		
