from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.properties import ObjectProperty
from mod.Color import ColorConversion, Colors
from kivy.lang import Builder

Builder.load_string("""
<LY_Background>:
	LCARS_CanvasLabel:
		pos: 118,446
		size: 672,23
		canvas.after:
			Color:
				rgba: root.elementscolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,8,8,0
	LCARS_CanvasLabel:
		pos: 118,11
		size: 672,23
		canvas.after:
			Color:
				rgba: root.elementscolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,8,8,0
	LCARS_CanvasLabel:
		pos: 11,11
		size: 107,38
		canvas.after:
			Color:
				rgba: root.elementscolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,0,0,32
	LCARS_CanvasLabel:
		pos: 11,431
		size: 107,38
		canvas.after:
			Color:
				rgba: root.elementscolor
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 32,0,0,0
	LCARS_CanvasLabel:
		pos: 107,417
		size: 40,29
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 12,0,0,0
	LCARS_CanvasLabel:
		pos: 107,34
		size: 40,29
		canvas.after:
			Color:
				rgba: root.black
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: 0,0,0,12
	LCARS_Label:
		text: 'MENU'
		pos: 42,435
		color: 0,0,0,1
		size: 35,18
		font_size: '28sp'
""")

class LY_Background(FloatLayout):
	id='LY_Background'
	elementscolor=Colors.lightyellow
	black=Colors.black
