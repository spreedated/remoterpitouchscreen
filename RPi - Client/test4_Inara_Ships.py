#!/usr/bin/python
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
os.environ['KIVY_AUDIO'] = 'sdl2' # <-- seems more stable, but cannot play MP3, WAV only
#os.environ['KIVY_AUDIO'] = 'gstplayer' # <-- can play WAV & MP3, also more accurate on timings, consider it a better alternative
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_IMAGE'] = 'sdl2'
os.environ['KIVY_VIDEO'] = 'null' # use for debug, no video, no warnings in console
#os.environ['KIVY_VIDEO'] = 'gstplayer' #using kivy.deps.gstreamer
#os.environ['KIVY_VIDEO'] = 'ffpyplayer' #i dont like ffpyplayer

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

		ships = [('U.S.S. Discovery', 'XK1337', 'Diamondback Explorer', '17,510,606 Cr', 17510606, 'HIP 13257 [Garnier City]', '/cmdr-fleet/112444/479253/'), ('U.S.s. Miner Alpha Two', 'XK1337', 'Python', '81,625,094 Cr', 81625094, 'LHS 3262 [Lacaille Prospect]', '/cmdr-fleet/112444/738588/'), ('U.S.S. Defiant AX', 'XK1337', 'Imperial Cutter', '1,009,775,387 Cr', 1009775387, 'Shinrarta Dezhra [Jameson Memorial]', '/cmdr-fleet/112444/823280/'), ('U.S.S. Defiant B', 'XK1337', 'Federal Corvette', '213,597,756 Cr', 213597756, 'Current Ship', '/cmdr-fleet/112444/962062/'), ('AX BLASTER', 'XK1337', 'Krait MkII', '112,518,433 Cr', 112518433, 'HIP 80242 [Csoma Ring]', '/cmdr-fleet/112444/987105/'), ('U.S.S. Discovery B', 'XK1337', 'Asp Explorer', '50,423,195 Cr', 50423195, 'Betel [Amphipolis]', '/cmdr-fleet/112444/1011066/')]
		ship_elements = []

		ships.sort(reverse=True)

		floaty_y = 0
		next_pos_y = 0
		ships_images = [
			('Diamondback Explorer','dbx2.png'),
			('Adder','adder2.png'),
			('Anaconda','anaconda2.png'),
			('Asp Explorer','aspx2.png'),
			('Fer-De-Lance','fdl2.png'),
			('Hauler','hauler2.png'),
			('Imperial Clipper','imp_clipper2.png'),
			('Imperial Courier','imp_courier2.png'),
			('Imperial Cutter','imp_cutter2.png'),
			('Imperial Eagle','imp_eagle2.png'),
			('Keelback','keelback2.png'),
			('Orca','orca2.png'),
			('Python','python2.png'),
			('Sidewinder','side2.png'),
			('Type-6 Transporter','type62.png'),
			('Type-7 Transporter','type72.png'),
			('Type-9 Transporter','type92.png'),
			('Viper MK III','vipermk32.png'),
			('Viper MK IV','vipermk42.png'),
			('Vulture','vulture2.png'),
				  ]
		for ship in ships:
			#print(ship)
			x = Label(size=(640,177), size_hint=(None,None), pos=(0,next_pos_y))
			with x.canvas.after:
				Color(1,1,1,0.2)
				RoundedRectangle(pos=x.pos, size=x.size, radius=(42,42,42,42))
			
			#Name
			x_Name_LBL = Label(text='Name', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+148, x.pos[1]+160), size=(250,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(250,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Name_LBL)
			x_Name = Label(text=ship[0], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+146, x.pos[1]+127), size=(240,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(240,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Name)

			#ID
			x_ID_LBL = Label(text='ID', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+148, x.pos[1]+105), size=(250,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(250,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_ID_LBL)
			x_ID = Label(text=ship[1], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+146, x.pos[1]+72), size=(80,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(80,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_ID)

			#Type
			x_Type_LBL = Label(text=ship[2], markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+10, x.pos[1]+145), size=(130,20), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='center', text_size=(130,20), shorten_from='right', split_str=' ', shorten=True)
			#with x_Type_LBL.canvas.before:
			#	Color(1,1,1,1)
			#	Rectangle(pos=x_Type_LBL.pos, size=x_Type_LBL.size)
			x.add_widget(x_Type_LBL)

			#Value Cr
			x_Value_LBL = Label(text='Name', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+398, x.pos[1]+160), size=(230,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(230,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Value_LBL)
			x_Value = Label(text=ship[3], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+398, x.pos[1]+127), size=(230,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(230,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Value)

			#Dock
			x_Dock_LBL = Label(text='Current Dock', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+148, x.pos[1]+43), size=(100,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(100,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Dock_LBL)
			x_Dock = Label(text=ship[5], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+146, x.pos[1]+10), size=(480,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(480,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Dock)

			#Picture
			img_string = None
			for xb in range(len(ships_images)):
				if str(ship[2]).lower() in str(ships_images[xb][0]).lower():
					img_string = ships_images[xb][1]

			if img_string != None:
				x_Picture = Image(source='img/edassets/ships/'+img_string,pos=(x.pos[0]+10, x.pos[1]+5), size=(125,142), size_hint=(None,None), id=self.id)
				x.add_widget(x_Picture)

			next_pos_y += 187
			self.floaty.add_widget(x)
			floaty_y += (x.size[1] + 10)
				

		#set size of floatlayout
		self.floaty.size = (self.floaty.size[0], floaty_y)

class MainApp(App):
	def build(self):
		self.title = 'Test'
		return MainLayout()

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()