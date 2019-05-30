from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.graphics.instructions import InstructionGroup
from mod.Color import ColorConversion
from mod.Sound import Sounds

class LCARS_LabelButton(ButtonBehavior, Label):
	def on_press(self):
		pass

class LCARS_ImageButton(ButtonBehavior, Image):
	def on_press(self):
		pass

class Buttons():
	# Left Navigation
	leftPositions = [(11,383),(11,336),(11,290),(11,243),(11,196),(11,150),(11,103),(11,56)]

	def Button_LeftNav(self, configClass, preloadClass, btnText, btnEnumPosition, btnEnumColor, id, btnClickSounds=0, action=None):
		btn = LCARS_LabelButton(pos=Buttons.leftPositions[btnEnumPosition], size=(96,40), size_hint=(None,None), id=id)
		with btn.canvas.before:
			if btnEnumColor == 0: #Yellow
				Color(1,1,0.2,1)
			if btnEnumColor == 1: #Light yellow
				Color(0.95,0.99,0.44,1)
			if btnEnumColor == 2: #Blue
				Color(0.6,0.8,1,1)
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=btnText, pos=(btn.pos[0]+2,btn.pos[1]-5), size=(50,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), id=id)
		btn_txt.bind(texture_size=btn_txt.setter('size'))
		btn.add_widget(btn_txt)

		elements = [btn,btn_txt]
		for x in elements:
			if action != None:
				x.bind(on_press=action)
			if configClass.clicksounds == 1:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
		self.add_widget(btn)
	# ###

	def RectangleButton(self, configClass, preloadClass, id, labeltext, action, position, width, iconImage=None, textsize='36sp', backgroundColor=(1,1,0,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		btn = LCARS_LabelButton(pos=(position[0],position[1]), size=(width,46), size_hint=(None,None), id=id)
		with btn.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=labeltext, pos=(position[0],position[1]), size=(width,44), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size=textsize, color=foregroundColor, markup=True, id=id, halign='center')
		btn.add_widget(btn_txt)

		elements = [btn,btn_txt]
		for x in elements:
			if action != None:
				x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
		self.add_widget(btn)

	def RoundedButton(self, configClass, preloadClass, id, labeltext, action, position, width, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(1,1,1,1), clickSound=True, soundFile=None):
		btn_center = LCARS_LabelButton(pos=(position[0],position[1]), size=(width,45), size_hint=(None,None), id=id)
		with btn_center.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			RoundedRectangle(pos=btn_center.pos, size=btn_center.size, radius=[23,23,23,23])
		btn_lbl = LCARS_LabelButton(text=labeltext, pos=(position[0],position[1]), size=(width,45), size_hint=(None,None), color=(foregroundColor[0],foregroundColor[1],foregroundColor[2],foregroundColor[3]), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, id=id, halign='center')
		btn_center.add_widget(btn_lbl)

		elements = [btn_center, btn_lbl]
		for x in elements:
			if action != None:
				x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
		self.add_widget(btn_center)

	def RoundedButtonSquare(self, configClass, preloadClass, id, labeltext, action, position, width, height, iconImage, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):	
		btn_Center = LCARS_LabelButton(pos=(position[0],position[1]), size=(width, height), size_hint=(None,None), id=id)
		with btn_Center.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			RoundedRectangle(pos=btn_Center.pos, size=btn_Center.size, radius=[30,30,30,30])

		btn_lbl = LCARS_LabelButton(text=labeltext, pos=(position[0],position[1]+12), size=(width,32), size_hint=(None,None), color=(foregroundColor[0],foregroundColor[1],foregroundColor[2],foregroundColor[3]), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, id=id, halign='center')

		btn_icon = LCARS_ImageButton(texture=preloadClass.returnPreloadedAsset(iconImage), pos=(position[0]+(width/2),position[1]+((height/100)*20)), size=(width+((width/100)*15), height-((height/100)*15)), size_hint=(None,None), id=id)
		btn_icon.pos=(btn_icon.pos[0]-(btn_icon.size[0]/2),btn_icon.pos[1])

		btn_Center.add_widget(btn_lbl)
		btn_Center.add_widget(btn_icon)

		elements = [btn_Center,btn_lbl,btn_icon]
		for x in elements:
			if action != None:
				x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
		self.add_widget(btn_Center)

	def Inara_RankButton(self, configClass, preloadClass, id, rankClass, rank, position, color):
		headline = Label(text=rankClass, pos=(position[0],position[1]+140), size=(140,25), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(color[0],color[1],color[2],color[3]), id=id)

		icon = Image(source='img/edassets/ranks/' + rank[1], pos=(position[0],position[1]+34), size_hint=(None,None), size=(140,104), id=id)

		btn = LCARS_LabelButton(pos=(position[0],position[1]), size=(140,30), size_hint=(None,None), id=self.id)
		with btn.canvas.before:
			Color(color[0],color[1],color[2],color[3])
			RoundedRectangle(pos=btn.pos, size=btn.size, radius=[12,12,12,12])

		btn_txt = Label(text=rank[0], pos=(position[0],position[1]), size=(140,30), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), id=id)
		
		elements = [headline,icon, btn,btn_txt]
		for x in elements:
			self.add_widget(x)

	def Inara_MainButton(self, mainClass, configClass, preloadClass, id, labeltext, position, action=None, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		btn = LCARS_LabelButton(pos=(position[0],position[1]), size=(197,43), size_hint=(None,None), id=self.id)
		with btn.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			RoundedRectangle(pos=btn.pos, size=btn.size, radius=[22,22,22,22])

		btn_txt = Label(text=labeltext, pos=(position[0],position[1]), size=(197,43), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size=textsize, color=(0,0,0,1), id=id)

		elements = [btn,btn_txt]
		for x in elements:
			if action != None:
				x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
			self.add_widget(x)

	def lblDisplayShip(self, mainClass, configClass, preloadClass, id, text, action=None, textsize='18sp', backgroundColor=(0,0.66,0.35,0.4), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		btn = LCARS_LabelButton(size=(640,177), size_hint_y=None, id=self.id)
		with btn.canvas.after:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			RoundedRectangle(pos=btn.pos, size=btn.size, radius=[42,42,42,42])

		btn_txt = Label(text=text, size=(197,43), size_hint_y=None, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, color=(1,1,1,1), id=id)

		btn.add_widget(btn_txt)

		elements = [btn]
		for x in elements:
			if action != None:
				x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
			mainClass.add_widget(x)