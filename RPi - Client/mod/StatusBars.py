import datetime
import time
import random
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

#region TopStatusBar
class TopStatusBar(FloatLayout):
	lbl_box = ObjectProperty()
	lbl_dot = ObjectProperty()
	lbl_time = ObjectProperty()

	def __init__(self, mainClass, lblText='neXn-Systems', **kwargs):
		super().__init__(**kwargs)
		id='TopStatusBar'
		#BlackBox behind
		maincnv = Label(pos=(457,445), size=(315,25), size_hint=(None,None), id=id)
		with maincnv.canvas.before:
			Color(0,0,0,1)
			Rectangle(pos=maincnv.pos, size=maincnv.size)

		self.lbl_box = Label(text=lblText, pos=(459,440), size=(225,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='28sp', id=id)
		self.lbl_box.bind(texture_size=self.lbl_box.setter('size'))
		self.lbl_dot = Label(text='', pos=(690,445), size=(5,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='28sp', id=id)
		self.lbl_time = Label(text='', pos=(705,445), size=(60,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='28sp', id=id)

		mainClass.add_widget(maincnv)
		mainClass.add_widget(self.lbl_box)
		mainClass.add_widget(self.lbl_dot)
		mainClass.add_widget(self.lbl_time)
		self.flash(None)

	def flash(self, instance):
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
class BottomStatusBar(FloatLayout):
	lbl_date = ObjectProperty()

	def __init__(self, mainClass, **kwargs):
		super().__init__(**kwargs)
		id='BottomStatusBar'
		#BlackBox behind
		maincnv = Label(pos=(206,10), size=(148,25), size_hint=(None,None), id=id)
		with maincnv.canvas.before:
			Color(0,0,0,1)
			Rectangle(pos=maincnv.pos, size=maincnv.size)
		mainClass.add_widget(maincnv)

		lbl_box = Label(text='stardate:', pos=(212,8), size=(70,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', id=id)
		lbl_box.bind(texture_size=lbl_box.setter('size'))
		self.add_widget(lbl_box)

		rndint = random.randint(10000,99999)
		self.lbl_date = Label(text=str(rndint) + '.00', pos=(289,8), size=(100,25), size_hint=(None,None), color=(0.99,0.61,0,1), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', id=id)
		self.lbl_date.bind(texture_size=self.lbl_date.setter('size'))
		mainClass.add_widget(self.lbl_date)

		self.timerDate(None)
		Clock.schedule_interval(self.timerDate, 45)

	def timerDate(self, instance):
		rndint = random.randint(00,99)
		self.lbl_date.text = self.lbl_date.text[:self.lbl_date.text.find('.')+1] + str("{:02d}".format(rndint))
#endregion