import configparser
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.logger import Logger
from mod.Color import ColorConversion
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from cryptography.fernet import Fernet

Builder.load_string("""
<PG_Configure_Inara>:
	username: username
	password: password
	apikey: apikey
	LCARS_CanvasLabel:
		pos: 118,342
		size: 328,90
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 20,0,0,20
	LCARS_Label:
		text: 'username'
		pos: 125,388
		text_size: 146,34
		size: 146,34
		font_size: '28sp'
		color: root.black
		halign: 'left'
	TextInput:
		pos: 274,388
		size: 163,34
		size_hint: None,None
		id: username

	LCARS_Label:
		text: 'password'
		pos: 125,352
		text_size: 146,34
		size: 146,34
		font_size: '28sp'
		color: root.black
		halign: 'left'
	TextInput:
		pos: 274,352
		size: 163,34
		size_hint: None,None
		password: True
		id: password



	LCARS_CanvasLabel:
		pos: 456,342
		size: 327,90
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,20,0
	LCARS_Label:
		text: 'api key'
		pos: 464,388
		text_size: 146,34
		size: 146,34
		font_size: '28sp'
		color: root.black
		halign: 'left'
	TextInput:
		pos: 614,348
		size: 158,75
		size_hint: None,None
		id: apikey
""")

class PG_Configure_Inara(FloatLayout):
	id='PG_Configure_Inara'

	mainClass = None
	configClass = None
	preloadClass = None
	infoClass = None

	mainelementcolor = ColorConversion.RGBA_to_Float(254,154,0)
	black = ColorConversion.RGBA_to_Float(0,0,0)

	username = ObjectProperty()
	password = ObjectProperty()
	apikey = ObjectProperty()
	passkey = None

	def __init__(self, mainClass, configClass, preloadClass, infoClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass
		self.infoClass = infoClass
		self.passkey = self.configClass.inara_pass_key

		unciphered =''
		try:
		    unciphered = Fernet(self.passkey).decrypt(self.configClass.inara_password).decode("utf-8")
		except :
		    pass
		
		self.username.text = self.configClass.inara_username
		self.password.text = unciphered
		self.apikey.text = self.configClass.inara_apikey

		#Save Button
		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'save configuration', self.saveConfig, (450,50), 288, '36sp', ColorConversion.RGBA_to_Float(181,0,6), ColorConversion.RGBA_to_Float(0,0,0))

	def saveConfig(self, instance):
		try:
		    #Change loop vars
			self.configClass.inara_username = self.username.text
			self.configClass.inara_apikey = self.apikey.text

			#Save to file
			config = configparser.ConfigParser()
			config.read(self.configClass.confFilePath)
			config.set('INARA','username', self.username.text)
			config.set('INARA','apikey', self.apikey.text)
			cipher_suite = Fernet(self.passkey.decode('UTF-8'))
			ciphered_pass = cipher_suite.encrypt(self.password.text.encode())   #required to be bytes
			config.set('INARA','password', ciphered_pass.decode('UTF-8'))

			with open(self.configClass.confFilePath, 'w') as configfile:
				config.write(configfile)
			
			self.configClass.inara_password = ciphered_pass

			Logger.info('CONFIG - INARA : Configuration saved!')
			self.showSave()

		except Exception as e:
			self.showFail()
			print(e)

	def showSave(self):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		x = Label(text='saved\nsuccessfully!', font_size='96sp', size_hint=(None,None), size=(665,166), pos=(118,166), font_name='fnt/lcarsgtj3.ttf', color=(0.99,0.61,0,1), halign='center', id=self.id)

		self.mainClass.add_widget(x)

	def showFail(self):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		x = Label(text='something went\nwrong!', font_size='96sp', size_hint=(None,None), size=(665,166), pos=(118,166), font_name='fnt/lcarsgtj3.ttf', color=(0.99,0.61,0,1),halign='center', id=self.id)

		self.mainClass.add_widget(x)