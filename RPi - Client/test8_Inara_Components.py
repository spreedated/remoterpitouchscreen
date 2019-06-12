#!/usr/bin/python
import os
os.environ["KIVY_NO_FILELOG"] = "1"
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
os.environ['KIVY_AUDIO'] = 'sdl2' # <-- seems more stable, but cannot play MP3, WAV only
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_IMAGE'] = 'sdl2'
os.environ['KIVY_VIDEO'] = 'null' # use for debug, no video, no warnings in console

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
from kivy.uix.textinput import TextInput
import math

Builder.load_string("""
<MainLayout>:
	floaty: floaty
	size_hint: None,None
	size: 665,383
	pos: 118,49
	FloatLayout:
		pos: 0,0
		size: 665,300
		size_hint: None,None
		id: floaty
""")

class MainLayout(ScrollView):
	floaty = ObjectProperty()

	components = [('Antimony', 18, '3.png'),('Arsenic', 57, '1.png'),('Boron', 0, '2.png'),('Cadmium', 100, '2.png'),('Carbon', 287, '0.png'),('Chromium', 80, '1.png'),('Germanium', 2, '1.png'),('Iron', 34, '0.png'),('Lead', 0, '0.png'),('Manganese', 127, '1.png'),('Mercury', 10, '2.png'),('Molybdenum', 57, '2.png'),('Nickel', 3, '0.png'),('Niobium', 43, '2.png'),('Phosphorus', 29, '0.png'),('Polonium', 1, '3.png'),('Rhenium', 0, '0.png'),('Ruthenium', 9, '3.png'),('Selenium', 11, '3.png'),('Sulphur', 234, '0.png'),('Technetium', 3, '3.png'),('Tellurium', 33, '3.png'),('Tin', 20, '2.png'),('Tungsten', 30, '2.png'),('Vanadium', 35, '1.png'),('Yttrium', 18, '3.png'),('Zinc', 54, '1.png'),('Zirconium', 12, '1.png'),('Basic Conductors', 9, '0.png'),('Bio-Mechanical Conduits', 60, '2.png'),('Biotech Conductors', 0, '4.png'),('Chemical Distillery', 21, '2.png'),('Chemical Manipulators', 8, '3.png'),('Chemical Processors', 15, '1.png'),('Chemical Storage Units', 18, '0.png'),('Compact Composites', 6, '0.png'),('Compound Shielding', 39, '3.png'),('Conductive Ceramics', 21, '2.png'),('Conductive Components', 19, '1.png'),('Conductive Polymers', 3, '3.png'),('Configurable Components', 15, '3.png'),('Core Dynamics Composites', 20, '4.png'),('Crystal Shards', 45, '0.png'),('Electrochemical Arrays', 14, '2.png'),('Exquisite Focus Crystals', 0, '4.png'),('Filament Composites', 15, '1.png'),('Flawed Focus Crystals', 33, '1.png'),('Focus Crystals', 53, '2.png'),('Galvanising Alloys', 60, '1.png'),('Grid Resistors', 67, '0.png'),('Guardian Power Cell', 208, '0.png'),('Guardian Power Conduit', 250, '1.png'),('Guardian Sentinel Weapon Parts', 171, '2.png'),('Guardian Technology Component', 6, '2.png'),('Guardian Wreckage Components', 195, '0.png'),('Heat Conduction Wiring', 19, '0.png'),('Heat Dispersion Plate', 48, '1.png'),('Heat Exchangers', 14, '2.png'),('Heat Resistant Ceramics', 18, '1.png'),('Heat Vanes', 7, '3.png'),('High Density Composites', 8, '2.png'),('Hybrid Capacitors', 23, '1.png'),('Imperial Shielding', 21, '4.png'),('Improvised Components', 9, '4.png'),('Mechanical Components', 30, '2.png'),('Mechanical Equipment', 34, '1.png'),('Mechanical Scrap', 67, '0.png'),('Military Grade Alloys', 0, '4.png'),('Military Supercapacitors', 10, '4.png'),('Pharmaceutical Isolators', 3, '4.png'),('Phase Alloys', 24, '2.png'),('Polymer Capacitors', 0, '3.png'),('Precipitated Alloys', 33, '2.png'),('Proprietary Composites', 24, '3.png'),('Propulsion Elements', 30, '2.png'),('Proto Heat Radiators', 0, '4.png'),('Proto Light Alloys', 13, '3.png'),('Proto Radiolic Alloys', 0, '4.png'),('Refined Focus Crystals', 3, '3.png'),('Salvaged Alloys', 5, '0.png'),('Sensor Fragment', 8, '4.png'),('Shield Emitters', 125, '1.png'),('Shielding Sensors', 78, '2.png'),('Tempered Alloys', 21, '0.png'),('Thargoid Carapace', 66, '1.png'),('Thargoid Energy Cell', 24, '2.png'),('Thargoid Organic Circuitry', 60, '4.png'),('Thargoid Technological Components', 36, '3.png'),('Thermic Alloys', 9, '3.png'),('Weapon Parts', 12, '2.png'),('Worn Shield Emitters', 115, '0.png'),('Wreckage Components', 60, '2.png'),('Aberrant Shield Pattern Analysis', 0, '3.png'),('Abnormal Compact Emissions Data', 0, '4.png'),('Adaptive Encryptors Capture', 1, '4.png'),('Anomalous Bulk Scan Data', 239, '0.png'),('Anomalous FSD Telemetry', 30, '1.png'),('Atypical Disrupted Wake Echoes', 143, '0.png'),('Atypical Encryption Archives', 0, '3.png'),('Classified Scan Databanks', 10, '2.png')]

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		#Build Floaty (FloatLayout inside ScrollView)
		self.components.sort(reverse=True)

		floaty_y = 0
		next_pos_x = 331 #Starting by building the right column first
		next_pos_y = 0
		halftime = int(math.ceil(len(self.components)/2)) #Calc when to break to next column, math.ceil for round UP

		for component in self.components:
			#print(ship)
			x = Label(size=(330,30), size_hint=(None,None), pos=(next_pos_x,next_pos_y))
			with x.canvas.before:
				Color(1,1,1,0.2)
				RoundedRectangle(size=x.size, size_hint=(None,None),  pos=x.pos, radius=(4,4,4,4))

			#Icon
			if component[2] != None:
				x_Icon = Image(source='img/matgrades/'+component[2], pos=(x.pos[0]+10, x.pos[1]+8), size=(13,13), size_hint=(None,None), id=self.id)
				x.add_widget(x_Icon)

			#Name
			x_Name = Label(text=component[0], markup=True, color=(1,1,1,0.8), pos=(x.pos[0]+30, x.pos[1]+1), size=(260,x.size[1]), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='20sp', id=self.id, halign='left', text_size=(260,x.size[1]), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Name)

			#Have
			x_Have = Label(text=str(component[1]), markup=True, color=(1,1,1,1), pos=(x.pos[0]+295, x.pos[1]+1), size=(30,x.size[1]), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', id=self.id, halign='right', text_size=(30,x.size[1]), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Have)

			addup = x.size[1] + 1
			next_pos_y += addup

			#check when to switch to next column
			halftime -= 1
			if halftime == 0:
				next_pos_x = 0
				next_pos_y = 0
			elif halftime >= -1:
				floaty_y += (addup)

			self.floaty.add_widget(x)
			
		#set size of floatlayout
		self.floaty.size = (self.floaty.size[0], (floaty_y))

	def printme(self, instance):
		print(self.textinput.text)

class MainApp(App):
	def build(self):
		self.title = 'Test'
		return MainLayout()

if __name__ == '__main__':
	#Window.borderless = True
	Window.size = (800, 480)
	MainApp().run()
