from kivy.logger import Logger
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

class RemovesClears():

	def clear_pages(className):
		exclusions =['mainBackground','btnLeftNavigation', 'BottomStatusBar','TopStatusBar']
		for x in range(8):
			for child in className.children:
				if child.id != None:
					if child.id not in exclusions:
						if type(child) == Video:
							child.unload()
						if type(child) == VideoPlayer:
							child.state = 'stop'
						#className.remove_widget(child)
						className.clear_widgets([child])
		Logger.info('PageFunction : Pages cleared')

	def remove_mywidget(className, widget_id):
		for x in range(5):
			for child in className.children:
				if child.id != None:
					if widget_id in child.id:
						if type(child) == Video:
							child.unload()
						if type(child) == VideoPlayer:
							child.state = 'stop'
						#className.remove_widget(child)
						className.clear_widgets([child])
