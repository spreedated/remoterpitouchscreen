import os
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.logger import Logger
from kivy.lang import Builder
from mod.Controls import Buttons

class PG_Ship_Controls(FloatLayout):
	id='PG_Ship_Controls'

	configClass = None

	pos_first_row = [(118,331),(259,331),(400,331),(541,331),(682,331)]
	pos_second_row = [(118,190),(259,190),(400,190),(541,190),(682,190)]
	pos_third_row = [(118,49),(259,49),(400,49),(541,49),(682,49)]

	def __init__(self, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.configClass = configClass

		#First Row
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'fsd', self.pos_first_row[0], 100, lambda a: self.sendKeys(['{L}']))
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'cruise', self.pos_first_row[1], 100, lambda a: self.sendKeys(['{K}']))
		#Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'route', self.pos_first_row[2], 100)
		#Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'news', self.pos_first_row[3], 100)
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'flight\nasst', self.pos_first_row[4], 100, lambda a: self.sendKeys(['{-}']))

		#Second Row
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'heat\nsink', self.pos_second_row[0], 100, lambda a: self.sendKeys(['{H}']))
		#Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, '---', self.pos_second_row[1], 100)
		#Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'chaff', self.pos_second_row[2], 100)
		#Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'ecm', self.pos_second_row[3], 100)
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'shield\ncell', self.pos_second_row[4], 100, lambda a: self.sendKeys(['{U}']))

		#Third Row
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'gear', self.pos_third_row[0], 100, lambda a: self.sendKeys(['{I}']))
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'scoop', self.pos_third_row[1], 100, lambda a: self.sendKeys(['{C}']))
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'hard\npoints', self.pos_third_row[2], 100, lambda a: self.sendKeys(['{J}']))
		#Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'silent\nrng', self.pos_third_row[3], 100)
		Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, 'lights', self.pos_third_row[4], 100, lambda a: self.sendKeys(['{0}']))

		if configClass.debug:
			Logger.info('PG_Ship_Controls : Loaded!')

	def sendKeys(self, sequence):
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)