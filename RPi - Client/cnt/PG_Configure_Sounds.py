import configparser
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.audio import Sound
from kivy.logger import Logger
from mod.Color import ColorConversion, Colors
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from mod.Sound import Sounds

Builder.load_string("""
<PG_Configure_Sounds>:
	overallVolumeSlider: overallVolumeSlider
	overallVolumePercent: overallVolumePercent
	clickSndSwitch: clickSndSwitch
	additionalSndSwitch: additionalSndSwitch

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
		text: 'overall volume'
		pos: 125,388
		text_size: 146,34
		size: 146,34
		font_size: '28sp'
		color: root.black
		halign: 'left'
	Slider:
		pos: 274,388
		size: 163,34
		size_hint: None,None
		range: (0,100)
		orientation: 'horizontal'
		step: 1
		id: overallVolumeSlider
	LCARS_Label:
		font_size: '28sp'
		color: root.black
		pos: 274,352
		size: 163,34
		text_size: 163,34
		halign: 'center'
		size_hint: None,None
		password: True
		id: overallVolumePercent
		
	#ClickSounds
	LCARS_CanvasLabel:
		pos: 456,380
		size: 327,52
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,20,0
	LCARS_Label:
		text: 'clicksounds'
		pos: 464,388
		text_size: 146,34
		size: 146,34
		font_size: '28sp'
		color: root.black
		halign: 'left'
	Switch:
		pos: 614,388
		size: 158,34
		size_hint: None,None
		id: clickSndSwitch

	#Additional Sounds
	LCARS_CanvasLabel:
		pos: 456,322
		size: 327,52
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,20,0
	LCARS_Label:
		text: 'additional sounds'
		pos: 464,331
		text_size: 146,34
		size: 146,34
		font_size: '28sp'
		color: root.black
		halign: 'left'
	Switch:
		pos: 614,331
		size: 158,34
		size_hint: None,None
		id: additionalSndSwitch
""")

class PG_Configure_Sounds(FloatLayout):
	id='PG_Configure_Sounds'

	mainClass = None
	configClass = None
	preloadClass = None
	infoClass = None

	mainelementcolor = Colors.lightBlue
	black = Colors.black

	overallVolumeSlider = ObjectProperty()
	overallVolumePercent = ObjectProperty()
	clickSndSwitch = ObjectProperty()
	additionalSndSwitch = ObjectProperty()

	def __init__(self, mainClass, configClass, preloadClass, infoClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass
		self.infoClass = infoClass
		
		#Overall Volume
		self.overallVolumeSlider.value = self.configClass.volume
		self.overallVolumePercent.text = str(int(self.overallVolumeSlider.value)) + ' %'
		self.overallVolumeSlider.bind(on_touch_move=self.UpdateSlider)
		self.overallVolumeSlider.bind(on_touch_up=self.PlayExampleSound)

		#ClickSound Switch
		self.clickSndSwitch.active = self.configClass.clicksounds

		#AdditionalSound Switch
		self.additionalSndSwitch.active = self.configClass.additionalSounds

		##Save Button
		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'save configuration', self.saveConfig, (450,50), 288, '36sp', Colors.darkRed, Colors.black)

	def UpdateSlider(self, instance, mouseMotionEventPosition):
		self.overallVolumePercent.text = str(int(self.overallVolumeSlider.value)) + ' %'

	def PlayExampleSound(self, instance, mouseMotionEventPosition):
		if 275 <= mouseMotionEventPosition.pos[0] <= 440 and 370 <= mouseMotionEventPosition.pos[1] <= 420: #Play only if between slider boundaries
			self.configClass.volume = self.overallVolumeSlider.value
			Sounds.PlaySound(self.preloadClass, self.configClass, 'input_rcvd.wav')

	def saveConfig(self, instance):
		try:
		    #Change loop vars
			self.configClass.volume = self.overallVolumeSlider.value
			self.configClass.clicksounds = self.clickSndSwitch.active
			self.configClass.additionalSounds = self.additionalSndSwitch.active

			#Save to file
			config = configparser.ConfigParser()
			config.read(self.configClass.confFilePath)
			config.set('SOUND','volume', str(int(self.overallVolumeSlider.value)))
			config.set('SOUND','clicksounds', str(int(self.clickSndSwitch.active)))
			config.set('SOUND','additionalSounds', str(int(self.additionalSndSwitch.active)))
			
			with open(self.configClass.confFilePath, 'w') as configfile:
				config.write(configfile)

			Logger.info('CONFIG - SOUND : Configuration saved!')
			self.showSave()

		except Exception as e:
			self.showFail()
			print(str(e))

	def showSave(self):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		x = Label(text='saved\nsuccessfully!', font_size='96sp', size_hint=(None,None), size=(665,166), pos=(118,166), font_name='fnt/lcarsgtj3.ttf', color=Colors.standardFont, halign='center', id=self.id)

		self.mainClass.add_widget(x)

	def showFail(self):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		x = Label(text='something went\nwrong!', font_size='96sp', size_hint=(None,None), size=(665,166), pos=(118,166), font_name='fnt/lcarsgtj3.ttf', color=Colors.standardFont, halign='center', id=self.id)

		self.mainClass.add_widget(x)