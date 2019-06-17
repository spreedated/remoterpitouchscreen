from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from mod.Color import Colors
from mod.Controls import *
from mod.RemovesClears import RemovesClears
from cnt.PG_Configure_Inara import *
from cnt.PG_Configure_Sounds import *

Builder.load_string("""
<PG_Configure>:
	LCARS_CanvasLabel:
		pos: 118,369
		size: 270,62
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 20,0,0,20
	LCARS_CanvasLabel:
		pos: 388,309
		size: 41,122
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,0,0
	LCARS_CanvasLabel:
		pos: 358,339
		size: 30,30
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			Rectangle:
				size: self.size
				pos: self.pos
	LCARS_CanvasLabel:
		pos: 358,339
		size: 30,30
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,0,0
	LCARS_CanvasLabel:
		pos: 512,369
		size: 270,62
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,20,0
	LCARS_CanvasLabel:
		pos: 472,309
		size: 41,122
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 20,0,0,0
	LCARS_CanvasLabel:
		pos: 513,339
		size: 30,30
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			Rectangle:
				size: self.size
				pos: self.pos
	LCARS_CanvasLabel:
		pos: 513,339
		size: 30,30
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 20,0,0,0
	LCARS_CanvasLabel:
		pos: 358,339
		size: 30,30
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,0,0
	LCARS_CanvasLabel:
		pos: 118,49
		size: 270,62
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 20,0,0,20
	LCARS_CanvasLabel:
		pos: 388,49
		size: 41,122
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,0,20,0
	LCARS_CanvasLabel:
		pos: 358,111
		size: 30,30
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			Rectangle:
				size: self.size
				pos: self.pos
	LCARS_CanvasLabel:
		pos: 358,111
		size: 30,30
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,0,20,0
	LCARS_CanvasLabel:
		pos: 512,49
		size: 270,62
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,20,20,0
	LCARS_CanvasLabel:
		pos: 472,49
		size: 41,122
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,0,0,20
	LCARS_CanvasLabel:
		pos: 513,111
		size: 30,30
		canvas.after:
			Color:
				rgba: root.mainelementcolor
			Rectangle:
				size: self.size
				pos: self.pos
	LCARS_CanvasLabel:
		pos: 513,111
		size: 30,30
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,0,0,20
	LCARS_CanvasLabel:
		pos: 388,175
		size: 41,130
		canvas.after:
			Color:
				rgba: root.contentelementcolor
			Rectangle:
				size: self.size
				pos: self.pos
	LCARS_CanvasLabel:
		pos: 472,175
		size: 41,130
		canvas.after:
			Color:
				rgba: root.contentelementcolor
			Rectangle:
				size: self.size
				pos: self.pos
""")

class PG_Configure(FloatLayout):
	id='PG_Configure'

	mainClass = None
	configClass = None
	preloadClass = None
	infoClass = None

	mainelementcolor = Colors.skyBlue
	black = Colors.black
	contentelementcolor = Colors.lightBlue

	leftSidePositions = [(125,315),(255,315),(125,250),(255,250),(125,184),(255,184),(125,118),(255,118)]
	rightSidePositions = [(518,315),(648,315),(518,250),(648,250),(518,184),(648,184),(518,118),(648,118)]
	rads = [(15,0,0,15), (0,15,15,0)] # 0 = leftSide buttons, 1 = rightSide buttons

	def __init__(self, mainClass, configClass, preloadClass, infoClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass
		self.infoClass = infoClass

		#Inara
		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'inara', lambda a: self.Goto_ChildPage('inara'), self.leftSidePositions[0], 127, '24sp', Colors.yellow, Colors.black, rad=self.rads[0])
		#Sound
		Buttons.RoundedButton(self, self.configClass, self.preloadClass, self.id, 'sounds', lambda a: self.Goto_ChildPage('sound'), self.rightSidePositions[1], 127, '24sp', Colors.yellow, Colors.black, rad=self.rads[1])

	def Goto_ChildPage(self, page):
		#Clear page of Main
		RemovesClears.remove_mywidget(self.mainClass, self.id)
		if page == 'inara':
			self.mainClass.add_widget(PG_Configure_Inara(self.mainClass, self.configClass, self.preloadClass, self.infoClass))
		if page == 'sound':
			self.mainClass.add_widget(PG_Configure_Sounds(self.mainClass, self.configClass, self.preloadClass, self.infoClass))
