import os
import time
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from mod.Color import ColorConversion
from mod.Controls import *
from mod.RemovesClears import RemovesClears

class ElitePIPSPage(FloatLayout):
	id='ElitePIPS'

	mainClass = None
	configClass = None
	preloadClass = None

	def __init__(self, mainClass, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.mainClass = mainClass
		self.configClass = configClass
		self.preloadClass = preloadClass

		self.page()

	def page(self):
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'engines', self.btn_speed, (118,371),233)
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'weapons', self.btn_weapons, (118,313),233)
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'system', self.btn_system, (118,256),233)
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'reset', self.btn_reset, (118,198),233)

		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'Combat turn', self.btn_combatturn, (538,340),233, backgroundColor=ColorConversion.RGBA_to_Float(153,205,255), soundFile='man_combatturn.wav')
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'Alpha Strike', self.btn_alphastrike, (494,255),233, backgroundColor=ColorConversion.RGBA_to_Float(181,0,6), soundFile='man_alphastrike.wav')
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'Head to Head', self.btn_headtohead, (494,170),233, backgroundColor=ColorConversion.RGBA_to_Float(181,0,6), soundFile='man_headtohead.wav')
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'Omega one', self.btn_omegaone, (185,85),233, backgroundColor=ColorConversion.RGBA_to_Float(0,168,89), soundFile='man_omegaone.wav')
		Buttons.RectangleButton(self.mainClass, self.configClass, self.preloadClass, self.id, 'Omega two', self.btn_omegatwo, (471,85),233, backgroundColor=ColorConversion.RGBA_to_Float(0,168,89), soundFile='man_omegatwo.wav')

	def btn_combatturn(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_alphastrike(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{RIGHT}', '{LEFT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_headtohead(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{LEFT}', '{RIGHT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_omegaone(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{LEFT}', '{LEFT}', '{UP}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_omegatwo(self, instance):
		sequence = ['{DOWN}', '{LEFT}', '{LEFT}', '{UP}', '{UP}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_reset(self, instance):
		os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key {DOWN}')

	def btn_system(self, instance):
		sequence = ['{DOWN}', '{LEFT}', '{LEFT}', '{LEFT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_weapons(self, instance):
		sequence = ['{DOWN}', '{RIGHT}', '{RIGHT}', '{RIGHT}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)

	def btn_speed(self, instance):
		sequence = ['{DOWN}', '{UP}', '{UP}', '{UP}']
		for key in sequence:
			os.system('python "' + os.getcwd() + '/'+self.configClass.socketfile+'" key ' + key)
