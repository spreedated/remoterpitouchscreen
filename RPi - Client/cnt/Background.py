from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from mod.Color import ColorConversion

class MainBackground(FloatLayout):
	id='mainBackground'

	def __init__(self, mainClass, **kwargs):
		super().__init__(**kwargs)

		elementscolor=ColorConversion.RGBA_to_Float(241,223,111)

		top = Label(pos=(118,446), size=(672,23), size_hint=(None,None), id=self.id)
		with top.canvas.after:
			Color(elementscolor[0],elementscolor[1],elementscolor[2],elementscolor[3])
			RoundedRectangle(size=top.size, pos=top.pos, radius=[0,8,8,0])
		mainClass.add_widget(top)

		bottom = Label(pos=(118,11), size=(672,23), size_hint=(None,None), id=self.id)
		with bottom.canvas.after:
			Color(elementscolor[0],elementscolor[1],elementscolor[2],elementscolor[3])
			RoundedRectangle(size=bottom.size, pos=bottom.pos, radius=[0,8,8,0])
		mainClass.add_widget(bottom)

		bottomCorner = Label(pos=(11,11), size=(107,38), size_hint=(None,None), id=self.id)
		with bottomCorner.canvas.after:
			Color(elementscolor[0],elementscolor[1],elementscolor[2],elementscolor[3])
			RoundedRectangle(size=bottomCorner.size, pos=bottomCorner.pos, radius=[0,0,0,32])
		mainClass.add_widget(bottomCorner)

		topCorner = Label(pos=(11,431), size=(107,38), size_hint=(None,None), id=self.id)
		with topCorner.canvas.after:
			Color(elementscolor[0],elementscolor[1],elementscolor[2],elementscolor[3])
			RoundedRectangle(size=topCorner.size, pos=topCorner.pos, radius=[32,0,0,0])
		mainClass.add_widget(topCorner)

		topblacken = Label(pos=(108,431), size=(10,15), size_hint=(None,None), id=self.id)
		topblacken_col=color=ColorConversion.RGBA_to_Float(0,0,0)
		with topblacken.canvas.after:
			Color(topblacken_col[0],topblacken_col[1],topblacken_col[2],topblacken_col[3])
			RoundedRectangle(size=topblacken.size, pos=topblacken.pos, radius=[5,0,0,0])
		mainClass.add_widget(topblacken)

		bottomblacken = Label(pos=(108,34), size=(10,15), size_hint=(None,None), id=self.id)
		bottomblacken_col=color=ColorConversion.RGBA_to_Float(0,0,0)
		with bottomblacken.canvas.after:
			Color(bottomblacken_col[0],bottomblacken_col[1],bottomblacken_col[2],bottomblacken_col[3])
			RoundedRectangle(size=bottomblacken.size, pos=bottomblacken.pos, radius=[0,0,0,5])
		mainClass.add_widget(bottomblacken)

		txt_menu = Label(text='MENU', pos=(42,435), size=(35,18), size_hint=(None,None), color=(0,0,0,1), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size='28 sp', id=self.id)
		mainClass.add_widget(txt_menu)
