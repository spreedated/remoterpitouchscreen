from kivy.logger import Logger
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

class RemovesClears():
	def clear_pages(className):
		for x in range(8):
			for child in className.children:
				if child.id != None:
					for page in className.Pages:
						if page in child.id:
							if type(child) == Video:
								child.unload()
							if type(child) == VideoPlayer:
								child.state = 'stop'
							className.remove_widget(child)
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
						className.remove_widget(child)
