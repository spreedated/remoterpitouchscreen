from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from mod.Sound import *

Builder.load_string("""
<PG_Exit>:
	LCARS_Label:
		text: 'COMPUTER CORE\\nSHUTDOWN'
		pos: 118,251
		size: 665,166
		halign: 'center'
		font_size: '96sp'
""")

class PG_Exit(FloatLayout):
	id='PG_Exit'

	mainClass = None
	configClass = None
	preloadClass = None

	def __init__(self, mainClass, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass

		#Sounds
		exitButtonSnd = None
		if self.configClass.additionalSounds:
			exitButtonSnd = 'beep.wav'

		Buttons.RoundedButton(self.mainClass, self.configClass, self.preloadClass, self.id + '_auth', '--- AUTHORIZE ---', self.exit_page1, (239,167), 411, soundFile=exitButtonSnd)

	def exit_page1(self, instance):
		RemovesClears.remove_mywidget(self.mainClass, 'Exit_auth')
		Buttons.RoundedButton(self.mainClass, self.configClass, self.preloadClass, self.id + '_auth', '--- CONFIRM ---', self.exit_page2, (328,81), 233, '42sp')
		if self.configClass.debug:
			Logger.info('PageFunction : Pageswitch - Exit 1')

	def exit_page2(self, instance):
		RemovesClears.clear_pages(self.mainClass)
		RemovesClears.remove_mywidget(self.mainClass, 'Navigation')

		if self.configClass.additionalSounds:
			Sounds.PlaySound(self.preloadClass, self.configClass, 'complete.wav')
			Clock.schedule_interval(lambda a: App.get_running_app().stop(), 4.5)
		else:
			App.get_running_app().stop()
