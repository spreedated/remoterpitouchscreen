from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.logger import Logger
from mod.Color import ColorConversion, Colors
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from cnt.PG_ShipControls_Controls import *
from cnt.PG_ShipControls_Limpets import *
from cnt.PG_ShipControls_Pips import *

Builder.load_string("""
<PG_ShipControls>:
	sidewinder: sidewinder
	Image:
		pos: 168,93
		size: 569,285
		size_hint: None,None
		id: sidewinder
		canvas.after:

			#Ship Controls
			Color:
				rgba: root.orange
			Line: 
				points: [(270,397),(332,397),(437,309),(437,246)]
				width: 2
				cap: 'round'
				joint: 'round'
				close: False
			
			#Limpets
			Color:
				rgba: root.blue
			Line: 
				points: [(450,152),(450,105),(461,69),(484,69)]
				width: 2
				cap: 'round'
				joint: 'round'
				close: False

			#PIPS
			Color:
				rgba: root.red
			Line: 
				points: [(617,397),(557,397),(458,309),(458,260)]
				width: 2
				cap: 'round'
				joint: 'round'
				close: False
""")

class PG_ShipControls(FloatLayout):
	id='PG_ShipControls'

	sidewinder = ObjectProperty()

	mainClass = None
	configClass = None
	preloadClass = None
	infoClass = None

	black = Colors.black
	orange = Colors.orange
	blue = Colors.skyBlue
	red = Colors.neonRed

	def __init__(self, mainClass, configClass, preloadClass, infoClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass
		self.infoClass = infoClass

		self.sidewinder.texture = self.preloadClass.returnPreloadedAsset('sidewinder_dorsal.png')

		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'ship ctrls', lambda a: self.Goto_ChildPage('shipctrls'), (138,374), 127, '24sp', self.orange, Colors.black, rad=(10,10,10,10))
		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'limpets', lambda a: self.Goto_ChildPage('limpets'), (491,49), 127, '24sp', self.blue, Colors.black, rad=(10,10,10,10))
		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'pips', lambda a: self.Goto_ChildPage('pips'), (623,374), 127, '24sp', self.red, Colors.black, rad=(10,10,10,10))

	def Goto_ChildPage(self, page):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		if page == 'shipctrls':
			self.mainClass.add_widget(PG_ShipControls_Controls(self.configClass, self.preloadClass))
		if page == 'pips':
			self.mainClass.add_widget(PG_ShipControls_Pips(self.configClass, self.preloadClass))
		if page == 'limpets':
			self.mainClass.add_widget(PG_ShipControls_Limpets(self.configClass, self.preloadClass))
