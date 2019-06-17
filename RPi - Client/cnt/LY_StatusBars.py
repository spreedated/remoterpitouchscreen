import datetime
import time
import random
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.lang import Builder
from mod.Color import Colors

Builder.load_string("""
<LY_TopStatusBar>:
	Label:
		pos: 457,445
		size: 315,25
		size_hint: None,None
		canvas.after:
			Color:
				rgba: 0,0,0,1
			Rectangle:
				pos: self.pos
				size: self.size
<LY_BottomStatusBar>:
	Label:
		pos: 206,10
		size: 148,25
		size_hint: None,None
		canvas.after:
			Color:
				rgba: 0,0,0,1
			Rectangle:
				pos: self.pos
				size: self.size
""")

#region TopStatusBar
class LY_TopStatusBar(FloatLayout):
	id='LY_TopStatusBar'

	lbl_box = ObjectProperty()
	lbl_dot = ObjectProperty()
	lbl_time = ObjectProperty()

	def __init__(self, lblText='neXn-Systems', **kwargs):
		super().__init__(**kwargs)

		self.lbl_box = Label(text=lblText, pos=(459,440), size=(225,25), size_hint=(None,None), color=Colors.standardFont, font_name='fnt/lcarsgtj3.ttf', font_size='28sp', id=self.id)
		self.lbl_box.bind(texture_size=self.lbl_box.setter('size'))
		self.lbl_dot = Label(text='', pos=(690,445), size=(5,25), size_hint=(None,None), color=Colors.standardFont, font_name='fnt/lcarsgtj3.ttf', font_size='28sp', id=self.id)
		self.lbl_time = Label(text='', pos=(705,445), size=(60,25), size_hint=(None,None), color=Colors.standardFont, font_name='fnt/lcarsgtj3.ttf', font_size='28sp', id=self.id)

		self.add_widget(self.lbl_box)
		self.add_widget(self.lbl_dot)
		self.add_widget(self.lbl_time)
		self.flash()

	def flash(self):
		Clock.schedule_interval(self.timer, 0.8)
		Clock.schedule_interval(self.timerTime, 0.1)

	def timer(self, instance):
		acc = self.lbl_dot.text
		if acc == '':
			self.lbl_dot.text = '•'
		else:
			self.lbl_dot.text = ''

	def timerTime(self, instance):
		now = datetime.datetime.now()
		self.lbl_time.text = now.strftime('%H:%M:%S')

	def changeCaption(self, caption):
		self.lbl_box.text = caption
#endregion

#region BottomStatusBar
class LY_BottomStatusBar(FloatLayout):
	id='LY_BottomStatusBar'

	lbl_date = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		lbl_box = Label(text='stardate:', pos=(212,8), size=(70,25), size_hint=(None,None), color=Colors.standardFont, font_name='fnt/lcarsgtj3.ttf', font_size='24sp', id=self.id)
		lbl_box.bind(texture_size=lbl_box.setter('size'))
		self.add_widget(lbl_box)

		rndint = random.randint(10000,99999)
		self.lbl_date = Label(text=str(rndint) + '.00', pos=(289,8), size=(100,25), size_hint=(None,None), color=Colors.standardFont, font_name='fnt/lcarsgtj3.ttf', font_size='24sp', id=self.id)
		self.lbl_date.bind(texture_size=self.lbl_date.setter('size'))
		self.add_widget(self.lbl_date)

		self.timerDate(None)
		Clock.schedule_interval(self.timerDate, 45)

	def timerDate(self, instance):
		rndint = random.randint(00,99)
		self.lbl_date.text = self.lbl_date.text[:self.lbl_date.text.find('.')+1] + str("{:02d}".format(rndint))
#endregion
