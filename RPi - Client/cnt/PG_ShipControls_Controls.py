import os
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from kivy.lang import Builder
from mod.Controls import Buttons
from mod.ServerEngine import *
from mod.Color import Colors

class PG_ShipControls_Controls(FloatLayout):
	id='PG_ShipControls_Controls'

	configClass = None

	pos_first_row = [(118,331),(259,331),(400,331),(541,331),(682,331)]
	pos_second_row = [(118,190),(259,190),(400,190),(541,190),(682,190)]
	pos_third_row = [(118,49),(259,49),(400,49),(541,49),(682,49)]

	def __init__(self, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.configClass = configClass

		elements = [configClass.button0_label, configClass.button1_label, configClass.button2_label, configClass.button3_label, configClass.button4_label, configClass.button5_label, configClass.button6_label, configClass.button7_label, configClass.button8_label, configClass.button9_label, configClass.button10_label, configClass.button11_label, configClass.button12_label, configClass.button13_label, configClass.button14_label]
		state = True
		for element in elements:
			if len(element) > 0:
				state = False

		if state:
			x = Label(size=(569,285), size_hint=(None,None), pos=(168,93), text='no bindings found\nin config.conf', font_name='fnt/lcarsgtj3.ttf', font_size='72sp', id=self.id, halign='center', color=Colors.standardFont)
			self.add_widget(x)
			if configClass.debug:
				Logger.info('PG_Ship_Controls : Loaded empty - no config entries!')
			return

		#First Row
		if configClass.button0_label != '' and configClass.button0_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button0_label.replace('\\n','\n')), self.pos_first_row[0], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button0_key)+'}']))
		if configClass.button1_label != '' and configClass.button1_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button1_label.replace('\\n','\n')), self.pos_first_row[1], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button1_key)+'}']))
		if configClass.button2_label != '' and configClass.button2_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button2_label.replace('\\n','\n')), self.pos_first_row[2], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button2_key)+'}']))
		if configClass.button3_label != '' and configClass.button3_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button3_label.replace('\\n','\n')), self.pos_first_row[3], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button3_key)+'}']))
		if configClass.button4_label != '' and configClass.button4_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button4_label.replace('\\n','\n')), self.pos_first_row[4], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button4_key)+'}']))

		#Second Row
		if configClass.button5_label != '' and configClass.button5_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button5_label.replace('\\n','\n')), self.pos_second_row[0], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button5_key)+'}']))
		if configClass.button6_label != '' and configClass.button6_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button6_label.replace('\\n','\n')), self.pos_second_row[1], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button6_key)+'}']))
		if configClass.button7_label != '' and configClass.button7_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button7_label.replace('\\n','\n')), self.pos_second_row[2], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button7_key)+'}']))
		if configClass.button8_label != '' and configClass.button8_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button8_label.replace('\\n','\n')), self.pos_second_row[3], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button8_key)+'}']))
		if configClass.button9_label != '' and configClass.button9_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button9_label.replace('\\n','\n')), self.pos_second_row[4], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button9_key)+'}']))

		#Third Row
		if configClass.button10_label != '' and configClass.button10_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button10_label.replace('\\n','\n')), self.pos_third_row[0], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button10_key)+'}']))
		if configClass.button11_label != '' and configClass.button11_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button11_label.replace('\\n','\n')), self.pos_third_row[1], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button11_key)+'}']))
		if configClass.button12_label != '' and configClass.button12_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button12_label.replace('\\n','\n')), self.pos_third_row[2], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button12_key)+'}']))
		if configClass.button13_label != '' and configClass.button13_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button13_label.replace('\\n','\n')), self.pos_third_row[3], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button13_key)+'}']))
		if configClass.button14_label != '' and configClass.button14_key != '':
			Buttons.RoundedSquareButton(self, configClass, preloadClass, self.id, str(configClass.button14_label.replace('\\n','\n')), self.pos_third_row[4], 100, lambda a: ServerEngine.sendKeys(self.configClass, ['{'+str(configClass.button14_key)+'}']))

		if configClass.debug:
			Logger.info('PG_Ship_Controls : Loaded!')
