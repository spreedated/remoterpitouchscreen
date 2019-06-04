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
		if configClass.button0_label != '' and configClass.button0_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button0_label.replace('\\n','\n')), self.pos_first_row[0], 100, lambda a: self.sendKeys(['{'+str(configClass.button0_key)+'}']))
		if configClass.button1_label != '' and configClass.button1_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button1_label.replace('\\n','\n')), self.pos_first_row[1], 100, lambda a: self.sendKeys(['{'+str(configClass.button1_key)+'}']))
		if configClass.button2_label != '' and configClass.button2_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button2_label.replace('\\n','\n')), self.pos_first_row[2], 100, lambda a: self.sendKeys(['{'+str(configClass.button2_key)+'}']))
		if configClass.button3_label != '' and configClass.button3_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button3_label.replace('\\n','\n')), self.pos_first_row[3], 100, lambda a: self.sendKeys(['{'+str(configClass.button3_key)+'}']))
		if configClass.button4_label != '' and configClass.button4_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button4_label.replace('\\n','\n')), self.pos_first_row[4], 100, lambda a: self.sendKeys(['{'+str(configClass.button4_key)+'}']))

		#Second Row
		if configClass.button5_label != '' and configClass.button5_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button5_label.replace('\\n','\n')), self.pos_second_row[0], 100, lambda a: self.sendKeys(['{'+str(configClass.button5_key)+'}']))
		if configClass.button6_label != '' and configClass.button6_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button6_label.replace('\\n','\n')), self.pos_second_row[1], 100, lambda a: self.sendKeys(['{'+str(configClass.button6_key)+'}']))
		if configClass.button7_label != '' and configClass.button7_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button7_label.replace('\\n','\n')), self.pos_second_row[2], 100, lambda a: self.sendKeys(['{'+str(configClass.button7_key)+'}']))
		if configClass.button8_label != '' and configClass.button8_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button8_label.replace('\\n','\n')), self.pos_second_row[3], 100, lambda a: self.sendKeys(['{'+str(configClass.button8_key)+'}']))
		if configClass.button9_label != '' and configClass.button9_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button9_label.replace('\\n','\n')), self.pos_second_row[4], 100, lambda a: self.sendKeys(['{'+str(configClass.button9_key)+'}']))

		#Third Row
		if configClass.button10_label != '' and configClass.button10_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button10_label.replace('\\n','\n')), self.pos_third_row[0], 100, lambda a: self.sendKeys(['{'+str(configClass.button10_key)+'}']))
		if configClass.button11_label != '' and configClass.button11_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button11_label.replace('\\n','\n')), self.pos_third_row[1], 100, lambda a: self.sendKeys(['{'+str(configClass.button11_key)+'}']))
		if configClass.button12_label != '' and configClass.button12_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button12_label.replace('\\n','\n')), self.pos_third_row[2], 100, lambda a: self.sendKeys(['{'+str(configClass.button12_key)+'}']))
		if configClass.button13_label != '' and configClass.button13_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button13_label.replace('\\n','\n')), self.pos_third_row[3], 100, lambda a: self.sendKeys(['{'+str(configClass.button13_key)+'}']))
		if configClass.button14_label != '' and configClass.button14_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button14_label.replace('\\n','\n')), self.pos_third_row[4], 100, lambda a: self.sendKeys(['{'+str(configClass.button14_key)+'}']))

		if configClass.debug:
			Logger.info('PG_Ship_Controls : Loaded!')

	def sendKeys(self, sequence):
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)