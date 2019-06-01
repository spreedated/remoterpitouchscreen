#!/usr/bin/python
import os
import sys
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty

Builder.load_string("""
<MainLayout>:
	floaty: floaty
	size_hint: None,None
	size: 665,383
	pos: 118,49
	FloatLayout:
		size: 665,800
		size_hint: None,None
		spacing: 10
		cols: 1
		col_default_width: 665
		col_force_default: True
		row_default_height: 177
		row_force_default: True
		id: floaty
""")

class MainLayout(ScrollView):

	floaty = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		ships = [('ship', '0'),('ship', '1'),('ship', '2'),('ship', '3'),('ship', '4')]
		ship_elements = []

		ships.sort(reverse=True)

		floaty_y = 0
		next_pos_y = 0
		for ship in ships:
			print(ship)
			x = Label(size=(640,177), size_hint=(None,None), pos=(0,next_pos_y))
			with x.canvas.after:
				Color(1,1,1,0.2)
				RoundedRectangle(pos=x.pos, size=x.size, radius=(42,42,42,42))
			xs = Label(size=(640,23), size_hint=(None,None), pos=(x.pos[0],x.pos[1]+90), text=ship[1], font_size='24sp')
			x.add_widget(xs)

			next_pos_y += 187
			self.floaty.add_widget(x)
			floaty_y += (x.size[1] + 10)
				

		#set size of floatlayout
		self.floaty.size = (self.floaty.size[0], floaty_y)

	def test(self, element):
		element.pos = (element.pos[0], 187)
		print(element.pos)

class MainApp(App):
	def build(self):
		self.title = 'Test'
		return MainLayout()

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()