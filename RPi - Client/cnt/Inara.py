import datetime
import time
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty, ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from mod.Color import ColorConversion
from mod.API_Works import API_Inara
from mod.Controls import *
from mod.Sound import Sounds
from mod.RemovesClears import RemovesClears

class Page_Inara(FloatLayout):
	id='inaracz'

	mainClass = None
	configClass = None
	preloadClass = None

	hexagon = ObjectProperty()
	hexagon_timer =  None

	def __init__(self, mainClass, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)
		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass

		self.Page_Main()

	def Page_Main(self):
		bg = Image(texture=self.preloadClass.returnPreloadedAsset('bg_inara.png'), pos=(118,81), size_hint=(None,None), size=(501,287), id=self.id)
		self.mainClass.add_widget(bg)

		self.DrawBackground()

		#animation
		self.hexagon = Image(texture=self.preloadClass.returnPreloadedAsset('inara_hexagon.png'), pos=(465,236), size_hint=(None,None), size=(40,23), id=self.id + '_hexagon')
		self.mainClass.add_widget(self.hexagon)

		self.animation()
		# ###

		#DEBUG
		Buttons.Inara_MainButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'fleet', (212,155), self.Goto_FleetPage, foregroundColor=ColorConversion.RGBA_to_Float(0,0,0))
		print('debug')
		return

		#Loading up INARA API Works
		lbl_info = Label(text='Loading...', pos=(204,288), size=(577,120), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='64sp', id=self.id, halign='center')
		self.mainClass.add_widget(lbl_info)
		
		x = API_Inara(self.configClass)
		output = None

		if x.errormsg != None:
			lbl_info.text = x.errormsg
			return # Stop here if something went wrong, like wrong api key
		
		Sounds.PlaySound(preloadClass, 'establishing_datalink.wav')
		self.mainClass.remove_widget(lbl_info)
		# ###

		#Add Rankings Combat Icons and Labels
		Buttons.Inara_RankButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'combat', x.cmdr_combatrank, (200,279), ColorConversion.RGBA_to_Float(181,0,6))
		Buttons.Inara_RankButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'trade', x.cmdr_traderank, (348,279), ColorConversion.RGBA_to_Float(254,154,0))
		Buttons.Inara_RankButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'exploration', x.cmdr_explorationrank, (495,279), ColorConversion.RGBA_to_Float(153,205,255))
		Buttons.Inara_RankButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'cqc', x.cmdr_cqcrank, (642,279), ColorConversion.RGBA_to_Float(237,26,33))

		#Buttons
		Buttons.Inara_MainButton(self, self.mainClass, self.configClass, self.preloadClass, self.id, 'fleet', (212,155), self.Goto_FleetPage, foregroundColor=ColorConversion.RGBA_to_Float(0,0,0))

	def animation(self):
		self.hexagon_timer = Clock.schedule_interval(lambda a: self.timer(), 0.02)

	direction = 'r'
	def timer(self):
		#kill timer if animation not active
		active = False
		for x in range(5):
			for child in self.mainClass.children:
				if child.id != None:
					if 'hexagon' in child.id:
						active = True

		if active == False:
			self.hexagon_timer.cancel()
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
		
	def DrawBackground(self):
		rect0 = Label(pos=(118,371), size=(78,60), size_hint=(None,None), id=self.id)
		rect0_col = ColorConversion.RGBA_to_Float(156,160,255)
		with rect0.canvas.after:
			Color(rect0_col[0],rect0_col[1],rect0_col[2],rect0_col[3])
			Rectangle(pos=rect0.pos, size=rect0.size)
		
		rect1 = Label(pos=(118,49), size=(78,30), size_hint=(None,None), id=self.id)
		rect1_col = ColorConversion.RGBA_to_Float(0,168,89)
		with rect1.canvas.after:
			Color(rect1_col[0],rect1_col[1],rect1_col[2],rect1_col[3])
			Rectangle(pos=rect1.pos, size=rect1.size)

		rect2 = Label(pos=(415,250), size=(26,13), size_hint=(None,None), id=self.id)
		rect2_col = ColorConversion.RGBA_to_Float(255,94,45)
		with rect2.canvas.after:
			Color(rect2_col[0],rect2_col[1],rect2_col[2],rect2_col[3])
			Rectangle(pos=rect2.pos, size=rect2.size)

		rect3 = Label(pos=(415,231), size=(26,13), size_hint=(None,None), id=self.id)
		rect3_col = ColorConversion.RGBA_to_Float(255,94,45)
		with rect3.canvas.after:
			Color(rect3_col[0],rect3_col[1],rect3_col[2],rect3_col[3])
			Rectangle(pos=rect3.pos, size=rect3.size)

		rect4 = Label(pos=(623,250), size=(114,13), size_hint=(None,None), id=self.id)
		rect4_col = ColorConversion.RGBA_to_Float(255,94,45)
		with rect4.canvas.after:
			Color(rect4_col[0],rect4_col[1],rect4_col[2],rect4_col[3])
			Rectangle(pos=rect4.pos, size=rect4.size)

		rect5 = Label(pos=(623,231), size=(114,13), size_hint=(None,None), id=self.id)
		rect5_col = ColorConversion.RGBA_to_Float(255,94,45)
		with rect5.canvas.after:
			Color(rect5_col[0],rect5_col[1],rect5_col[2],rect5_col[3])
			Rectangle(pos=rect5.pos, size=rect5.size)

		rect6 = Label(pos=(744,250), size=(26,13), size_hint=(None,None), id=self.id)
		rect6_col = ColorConversion.RGBA_to_Float(181,0,6)
		with rect6.canvas.after:
			Color(rect6_col[0],rect6_col[1],rect6_col[2],rect6_col[3])
			Rectangle(pos=rect6.pos, size=rect6.size)

		rect7 = Label(pos=(744,231), size=(26,13), size_hint=(None,None), id=self.id)
		rect7_col = ColorConversion.RGBA_to_Float(181,0,6)
		with rect7.canvas.after:
			Color(rect7_col[0],rect7_col[1],rect7_col[2],rect7_col[3])
			Rectangle(pos=rect7.pos, size=rect7.size)

		
		elements =[rect0,rect1,rect2,rect3,rect4,rect5,rect6,rect7]
		for x in elements:
			self.mainClass.add_widget(x)

	def Goto_FleetPage(self, instance):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)

	def Goto_Back_MainWindow(self):
		self.Page_Main()
		