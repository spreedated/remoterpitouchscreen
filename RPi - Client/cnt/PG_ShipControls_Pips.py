import os
import time
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from mod.Color import ColorConversion, Colors
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from mod.ServerEngine import *

class PG_ShipControls_Pips(FloatLayout):
	id='PG_ShipControls_Pips'

	configClass = None
	preloadClass = None

	def __init__(self, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.configClass = configClass
		self.preloadClass = preloadClass

		self.page()

	def page(self):
		#SoundVars
		cmbtsnd = None
		alphastrikesnd = None
		head2head = None
		omega1 = None
		omega2 = None
		if self.configClass.additionalSounds:
			cmbtsnd = 'man_combatturn.wav'
			alphastrikesnd = 'man_alphastrike.wav'
			head2head = 'man_headtohead.wav'
			omega1 = 'man_omegaone.wav'
			omega2 = 'man_omegatwo.wav'

		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'engines', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{UP}', '{UP}', '{UP}']), (118,371),233)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'weapons', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{RIGHT}', '{RIGHT}', '{RIGHT}']), (118,313),233)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'system', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{LEFT}', '{LEFT}', '{LEFT}']), (118,256),233)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'reset', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}']), (118,198),233)

		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'Combat turn', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{UP}', '{UP}', '{LEFT}']), (538,340),233, backgroundColor=Colors.lightBlue, soundFile=cmbtsnd)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'Alpha Strike', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{RIGHT}', '{RIGHT}', '{LEFT}', '{LEFT}']), (494,255),233, backgroundColor=Colors.darkRed, soundFile=alphastrikesnd)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'Head to Head', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{RIGHT}', '{LEFT}', '{RIGHT}', '{LEFT}']), (494,170),233, backgroundColor=Colors.darkRed, soundFile=head2head)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'Omega one', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{UP}', '{UP}', '{LEFT}', '{LEFT}', '{UP}']), (185,85),233, backgroundColor=Colors.green, soundFile=omega1)
		Buttons.RectangleButton(self, self.configClass, self.preloadClass, self.id, 'Omega two', lambda a: ServerEngine.sendKeys(self.configClass, ['{DOWN}', '{LEFT}', '{LEFT}', '{UP}', '{UP}', '{LEFT}']), (471,85),233, backgroundColor=Colors.green, soundFile=omega2)
