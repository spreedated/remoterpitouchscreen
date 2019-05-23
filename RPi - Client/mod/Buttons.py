from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior

class MyButton(ButtonBehavior, Label):
	def on_press(self):
		pass

class MyImageButton(ButtonBehavior, Image):
	def on_press(self):
		pass




