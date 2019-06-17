from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty, ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from mod.Color import ColorConversion
from mod.Controls import *
from mod.Sound import Sounds
from mod.RemovesClears import RemovesClears
from cnt.PG_Inara import *
from cnt.PG_Exit import *
from cnt.PG_Welcome import *
from cnt.PG_ShipControls import *
from cnt.PG_Configure import *
import mod.Information as ApplicationInfo

class NV_MainNavigation(FloatLayout):
	id='NV_MainNavigation'

	mainClass = None
	configClass = None
	preloadClass = None
	TopStatusBar = None
	infoClass = None

	def __init__(self, mainClass, configClass, preloadClass, topStatusBarClass, infoClass, **kwargs):
		super().__init__(**kwargs)
		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass
		self.TopStatusBar = topStatusBarClass
		self.infoClass = infoClass

		if self.configClass.debug == True:
			Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'debug', 1, 2, self.id, 1, lambda a: self.PageSwitch('test'))

		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'welcome', 0, 0, self.id, 1, lambda a: self.PageSwitch('welcome'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'inara', 2, 2, self.id, 1, lambda a: self.PageSwitch('inara'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'ship ctrls', 4, 0, self.id, 1, lambda a: self.PageSwitch('shipctrls'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'configure', 6, 0, self.id, 1, lambda a: self.PageSwitch('configure'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'exit', 7, 2, self.id, 1, lambda a: self.PageSwitch('exit'))

	def PageSwitch(self, page):
		RemovesClears.clear_pages(self.mainClass)

		if page == 'exit':
			self.TopStatusBar.changeCaption('shutdown')
			if self.configClass.debug == True:
				Logger.info('PageFunction : Pageswitch - Shutdown')
			self.mainClass.add_widget(PG_Exit(self.mainClass, self.configClass, self.preloadClass))
		if page == 'inara':
			self.TopStatusBar.changeCaption('inara')
			if self.configClass.debug == True:
				Logger.info('PageFunction : Pageswitch - Inara')
			self.mainClass.add_widget(PG_Inara(self.mainClass, self.configClass, self.preloadClass, self.infoClass))
		if page == 'welcome':
			self.TopStatusBar.changeCaption(ApplicationInfo.appFullName)
			if self.configClass.debug == True:
				Logger.info('PageFunction : Pageswitch - welcome')
			self.mainClass.add_widget(PG_Welcome(self.configClass, self.preloadClass))
		if page == 'shipctrls':
			self.TopStatusBar.changeCaption('ship controls')
			if self.configClass.debug == True:
				Logger.info('PageFunction : Pageswitch - ship controls')
			self.mainClass.add_widget(PG_ShipControls(self.mainClass, self.configClass, self.preloadClass, self.infoClass))
		if page == 'configure':
			self.TopStatusBar.changeCaption('configure')
			if self.configClass.debug == True:
				Logger.info('PageFunction : Pageswitch - configure')
			self.mainClass.add_widget(PG_Configure(self.mainClass, self.configClass, self.preloadClass, self.infoClass))
		if page == 'test':
			self.TopStatusBar.changeCaption('test')
			if self.configClass.debug == True:
				Logger.info('PageFunction : Pageswitch - test')
			print(self.infoClass.cmdr_combatrank)
