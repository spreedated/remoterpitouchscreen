from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from mod.Color import ColorConversion
from mod.Sound import Sounds

class MyButton(ButtonBehavior, Label):
	def on_press(self):
		pass

class MyImageButton(ButtonBehavior, Image):
	def on_press(self):
		pass

class Buttons():
	# Left Navigation
	leftPositions = [(11,383),(11,336),(11,290),(11,243),(11,196),(11,150),(11,103),(11,56)]

	def Button_LeftNav(self, configClass, preloadClass, btnText, btnEnumPosition, btnEnumColor, btnClickSounds=0, action=None):
		btn = MyButton(pos=Buttons.leftPositions[btnEnumPosition], size=(96,40), size_hint=(None,None), id='btnLeftNavigation')
		with btn.canvas.before:
			if btnEnumColor == 0: #Yellow
				Color(1,1,0.2,1)
			if btnEnumColor == 1: #Light yellow
				Color(0.95,0.99,0.44,1)
			if btnEnumColor == 2: #Blue
				Color(0.6,0.8,1,1)
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=btnText, pos=(btn.pos[0]+2,btn.pos[1]-5), size=(50,13), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', color=(0,0,0,1), id='btnLeftNavigation')
		btn_txt.bind(texture_size=btn_txt.setter('size'))

		elements = [btn,btn_txt]
		for x in elements:
			x.bind(on_press=action)
			if configClass.clicksounds == 1:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			self.add_widget(x)
	# ###

	def RectangleButton(self, configClass, preloadClass, id, labeltext, action, position, width, iconImage=None, textsize='36sp', backgroundColor=(1,1,0,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		btn = MyButton(pos=(position[0],position[1]), size=(width,46), size_hint=(None,None), id=id)
		with btn.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=labeltext, pos=(position[0],position[1]), size=(width,44), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size=textsize, color=foregroundColor, markup=True, id=id, halign='center')

		elements = [btn, btn_txt]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
			self.add_widget(x)

	def RoundedButton(self, configClass, preloadClass, id, images, labeltext, action, position, width, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(1,1,1,1), clickSound=True, soundFile=None):
		btn_left = MyImageButton(texture=preloadClass.returnPreloadedAsset(images[0]), pos=position, size_hint=(None,None), size=(23,46), id=id)
		btn_right = MyImageButton(texture=preloadClass.returnPreloadedAsset(images[1]), pos=(position[0]+19+width, position[1]), size_hint=(None,None), size=(23,46), id=id)
		btn_center = MyButton(pos=(position[0]+21,position[1]+1), size=(width,45), size_hint=(None,None), id=id)
		with btn_center.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_center.pos, size=btn_center.size)
		btn_lbl = MyButton(text=labeltext, pos=(position[0]+21,position[1]+7), size=(width,31), size_hint=(None,None), color=(foregroundColor[0],foregroundColor[1],foregroundColor[2],foregroundColor[3]), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, id=id, halign='center')

		elements = [btn_right,btn_left,btn_center,btn_lbl]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
			self.add_widget(x)

	def RoundedButtonSquare(self, configClass, preloadClass, id, cornerImages, labeltext, action, position, width, height, iconImage, textsize='48sp', backgroundColor=(0.71,0,0.02,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		width = width-64
		height = height-32
		btn_upLeft = MyImageButton(texture=preloadClass.returnPreloadedAsset(cornerImages[0]), pos=(position[0],position[1]+height), size_hint=(None,None), size=(32,32), id=id)
		btn_upRight = MyImageButton(texture=preloadClass.returnPreloadedAsset(cornerImages[1]), pos=(position[0]+width+33,position[1]+height), size_hint=(None,None), size=(32,32), id=id)
		btn_downLeft = MyImageButton(texture=preloadClass.returnPreloadedAsset(cornerImages[2]), pos=(position[0],position[1]), size_hint=(None,None), size=(32,32), id=id)
		btn_downRight = MyImageButton(texture=preloadClass.returnPreloadedAsset(cornerImages[3]), pos=(position[0]+width+33,position[1]-1), size_hint=(None,None), size=(32,32), id=id)

		btn_upCenter = MyButton(pos=(position[0]+32,position[1]+height), size=(width+2,32), size_hint=(None,None), id=id)
		with btn_upCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_upCenter.pos, size=btn_upCenter.size)
		btn_downCenter = MyButton(pos=(position[0]+32,position[1]), size=(width+2,32), size_hint=(None,None), id=id)
		with btn_downCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_downCenter.pos, size=btn_downCenter.size)

		btn_leftCenter = MyButton(pos=(position[0],position[1]+31), size=(32,(height-31)), size_hint=(None,None), id=id)
		with btn_leftCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_leftCenter.pos, size=btn_leftCenter.size)
		btn_rightCenter = MyButton(pos=(position[0]+width+32,position[1]+30), size=(32,(height-30)), size_hint=(None,None), id=id)
		with btn_rightCenter.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_rightCenter.pos, size=btn_rightCenter.size)

		btn_Center = MyButton(pos=(position[0]+32,position[1]+32), size=(width,(height-32)), size_hint=(None,None), id=id)
		with btn_Center.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn_Center.pos, size=btn_Center.size)

		btn_lbl = MyButton(text=labeltext, pos=(position[0],position[1]+12), size=(width+64,32), size_hint=(None,None), color=(foregroundColor[0],foregroundColor[1],foregroundColor[2],foregroundColor[3]), markup=True, font_name='fnt/lcarsgtj3.ttf', font_size=textsize, id=id, halign='center')

		btn_icon = MyImageButton(texture=preloadClass.returnPreloadedAsset(iconImage), pos=(position[0]+((width+64)/2),position[1]+(((height+32)/100)*30)), size=(width+(((width+64)/100)*15), height-(((height+32)/100)*15)), size_hint=(None,None), id=id)
		btn_icon.pos=(btn_icon.pos[0]-(btn_icon.size[0]/2),btn_icon.pos[1])

		elements = [btn_downRight,btn_downLeft,btn_upLeft,btn_upRight,btn_Center,btn_rightCenter,btn_leftCenter,btn_downCenter,btn_upCenter,btn_lbl,btn_icon]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=lambda a:Sounds.PlayClickSound(preloadClass))
			if soundFile != None:
				x.bind(on_press=lambda a:Sounds.PlaySound(preloadClass, soundFile))
			self.add_widget(x)
