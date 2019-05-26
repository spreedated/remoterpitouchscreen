from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from mod.Controls import *
from mod.RemovesClears import RemovesClears

class ExitPage(FloatLayout):
	id='Exit'

	mainClass = None
	configClass = None
	preloadClass = None

	def __init__(self, mainClass, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass

		lbl_shutdown = Label(text='COMPUTER CORE\nSHUTDOWN', pos=(282,256), size=(325,152), size_hint=(None,None), color=(0.99,0.61,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='96sp', id=self.id, halign='center')
		self.add_widget(lbl_shutdown)

		Buttons.RoundedButton(self.mainClass, self.configClass, self.preloadClass, self.id + '_auth', '--- AUTHORIZE ---', self.exit_page1, (239,167), 411, soundFile='beep.wav')

	def exit_page1(self, instance):
		RemovesClears.remove_mywidget(self.mainClass, 'Exit_auth')
		Buttons.RoundedButton(self.mainClass, self.configClass, self.preloadClass, self.id + '_auth', '--- CONFIRM ---', self.exit_page2, (328,81), 233, '42sp', soundFile='complete.wav')
		Logger.info('PageFunction : Pageswitch - Exit 1')

	def exit_page2(self, instance):
		RemovesClears.clear_pages(self.mainClass)
		RemovesClears.remove_mywidget(self.mainClass, 'Navigation')
		Clock.schedule_interval(lambda a: App.get_running_app().stop(), 4.5)
