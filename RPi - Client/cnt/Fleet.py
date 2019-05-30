from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.logger import Logger
from mod.Controls import *
from mod.RemovesClears import RemovesClears

class Fleet(FloatLayout):
	id='Fleet'

	mainClass = None
	configClass = None
	preloadClass = None

	def __init__(self, mainClass, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass

		#bar_inactive_color=[0,0,0,0]
		scr = ScrollView(pos=(118,49), size=(665,383), size_hint=(None,None), id=self.id, do_scroll_y=True, do_scroll_x=True, bar_inactive_color=[1,1,1,1])
		#with scr.canvas.before:
		#	Color(0.5,0.6,0.7,1)
		#	Rectangle(pos=scr.pos, size=scr.size)

		#t = FloatLayout(size=(665,470), pos=(0,0), size_hint=(None,None))
		#t = GridLayout(pos=(118,49), size=(665,1000), cols=1, size_hint=(None,None)) #, col_default_width=665, col_force_default=True, row_default_height=117, row_force_default=True
		t = StackLayout(pos=(118,49), size=(1000,1500), size_hint=(None,None)) #, orientation='lr-bt'

		#Buttons.lblDisplayShip(self, t, self.configClass, self.preloadClass, self.id, '')
		#Buttons.lblDisplayShip(self, t, self.configClass, self.preloadClass, self.id, 'test')
		#Buttons.lblDisplayShip(self, t, self.configClass, self.preloadClass, self.id, 'test2')
		
		#t.add_widget(Label(text='World 1', size=(665,117), size_hint_y=None))
		#t.add_widget(Label(text='World 2', size=(665,117), size_hint_y=None))
		#t.add_widget(Label(text='World 3', size=(665,117), size_hint_y=None))

		btn = LCARS_LabelButton(size=(640,177), size_hint=(None,None), id=self.id)
		with btn.canvas.after:
			Color(0,0.66,0.35,0.4)
			RoundedRectangle(pos=btn.pos, size=btn.size, radius=[42,42,42,42])

		btn0 = LCARS_LabelButton(size=(640,177), size_hint=(None,None), id=self.id)
		with btn0.canvas.after:
			Color(0,0.66,0.35,0.4)
			RoundedRectangle(pos=btn0.pos, size=btn0.size, radius=[42,42,42,42])

		t.add_widget(btn0)
		t.add_widget(btn)

		for child in t.children:
			print(child.id)

		#mainClass.add_widget(t)

		scr.add_widget(t)
		mainClass.add_widget(scr)
