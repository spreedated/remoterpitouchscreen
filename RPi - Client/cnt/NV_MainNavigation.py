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
from cnt.Elite_Limpets import *
from cnt.Elite_PIPS import *
from cnt.PG_Ship_Controls import *

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

		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'debug', 0, 2, self.id, 1, lambda a: self.PageSwitch('test'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'inara', 1, 2, self.id, 1, lambda a: self.PageSwitch('inara'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'welcome', 2, 0, self.id, 1, lambda a: self.PageSwitch('welcome'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'elite limpets', 4, 1, self.id, 1, lambda a: self.PageSwitch('limpets'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'elite pips', 5, 0, self.id, 1, lambda a: self.PageSwitch('pips'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'ship ctrls', 6, 0, self.id, 1, lambda a: self.PageSwitch('shipctrls'))
		Buttons.Button_LeftNav(self, self.configClass, self.preloadClass, 'exit', 7, 2, self.id, 1, lambda a: self.PageSwitch('exit'))

	def PageSwitch(self, page):
		RemovesClears.clear_pages(self.mainClass)

		if page == 'exit':
			self.TopStatusBar.changeCaption('shutdown')
			Logger.info('PageFunction : Pageswitch - Shutdown')
			self.mainClass.add_widget(PG_Exit(self.mainClass, self.configClass, self.preloadClass))
		if page == 'inara':
			self.TopStatusBar.changeCaption('inara')
			Logger.info('PageFunction : Pageswitch - Inara')
			self.mainClass.add_widget(PG_Inara(self.mainClass, self.configClass, self.preloadClass, self.infoClass))
		if page == 'welcome':
			self.TopStatusBar.changeCaption('elite lcars')
			Logger.info('PageFunction : Pageswitch - welcome')
			self.mainClass.add_widget(PG_Welcome(self.configClass, self.preloadClass))
		if page == 'limpets':
			self.TopStatusBar.changeCaption('elite limpets')
			Logger.info('PageFunction : Pageswitch - elite limpets')
			self.mainClass.add_widget(EliteLimpetsPage(self.mainClass, self.configClass, self.preloadClass))
		if page == 'pips':
			self.TopStatusBar.changeCaption('elite pips')
			Logger.info('PageFunction : Pageswitch - elite pips')
			self.mainClass.add_widget(ElitePIPSPage(self.mainClass, self.configClass, self.preloadClass))
		if page == 'shipctrls':
			self.TopStatusBar.changeCaption('ship controls')
			Logger.info('PageFunction : Pageswitch - ship controls')
			self.mainClass.add_widget(PG_Ship_Controls(self.configClass, self.preloadClass))
		if page == 'test':
			self.TopStatusBar.changeCaption('test')
			Logger.info('PageFunction : Pageswitch - test')
			print(self.infoClass.cmdr_combatrank)
