import os
import time
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from mod.Color import ColorConversion
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from mod.ServerEngine import *

class PG_ShipControls_Limpets(FloatLayout):
	id='PG_ShipControls_Limpets'

	configClass = None
	preloadClass = None

	def __init__(self, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.configClass = configClass
		self.preloadClass = preloadClass

		self.page()

	def page(self):
		btn_positions_first_row=[(124,251),(289,251),(453,251),(618,251)]
		btn_positions_second_row=[(124,49),(289,49),(453,49),(618,49)]

		#COLLECTOR
		Buttons.RoundedButtonSquare(self, self.configClass, self.preloadClass, self.id, 'COLLECTOR', lambda a: ServerEngine.sendKeys(self.configClass, ['{VK_NUMPAD4}', '{VK_NUMPAD4}', '{VK_ADD}', '{VK_NUMPAD4}']), btn_positions_first_row[3], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(254,154,0))
		#DECON
		Buttons.RoundedButtonSquare(self, self.configClass, self.preloadClass, self.id, 'DECON', lambda a: ServerEngine.sendKeys(self.configClass, ['{VK_NUMPAD4}', '{VK_NUMPAD0}', '{VK_NUMPAD6}']), btn_positions_first_row[0], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(153,205,255))
		#REPAIR
		Buttons.RoundedButtonSquare(self, self.configClass, self.preloadClass, self.id, 'REPAIR', lambda a: ServerEngine.sendKeys(self.configClass, ['{VK_NUMPAD4}', '{VK_ADD}', '{VK_NUMPAD6}']), btn_positions_second_row[2], 150, 180, 'limpet_black.png', '48sp', ColorConversion.RGBA_to_Float(0,168,89))

