from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from mod.Color import ColorConversion

class MyButton(ButtonBehavior, Label):
	def on_press(self):
		pass

class MyImageButton(ButtonBehavior, Image):
	def on_press(self):
		pass

class ButtonClasses():
	def RectangleButton(self, configClass, id, labeltext, action, position, width, iconImage=None, textsize='36sp', backgroundColor=(1,1,0,1), foregroundColor=(0,0,0,1), clickSound=True, soundFile=None):
		btn = MyButton(pos=(position[0],position[1]), size=(width,46), size_hint=(None,None), id=id)
		with btn.canvas.before:
			Color(backgroundColor[0],backgroundColor[1],backgroundColor[2],backgroundColor[3])
			Rectangle(pos=btn.pos, size=btn.size)
		btn_txt = Label(text=labeltext, pos=(position[0],position[1]), size=(width,44), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size=textsize, color=foregroundColor, markup=True, id=id, halign='center')

		elements = [btn, btn_txt]
		for x in elements:
			x.bind(on_press=action)
			if clickSound and configClass.clicksounds == 1 and soundFile == None:
				x.bind(on_press=self.PlayClickSound)
			if soundFile != None:
				x.bind(on_press=lambda a:self.PlaySound(soundFile))
			self.add_widget(x)
