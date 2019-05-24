import os
import threading
from kivy.logger import Logger
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

class PreloadAssets(object):
	preloadedAssets = []

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#preload IMAGES
		count = 0
		for file in os.listdir("img"):
			if file.endswith(".png"):
				count+=1
				self.preloadedAssets.append([file, Image(source='img/'+file).texture])
		if count == 1:
			Logger.info('Preload : one Imagefile loaded to memory as textures')
		else:
			Logger.info('Preload : ' + str(count) + ' Imagefiles loaded to memory as textures')
		#preload SOUNDS
		count = 0
		for r,d,f in os.walk('snd'):
			for file in os.listdir(r):
					if file.endswith(".wav") or file.endswith(".mp3"):
						count+=1
						self.preloadedAssets.append([os.path.join(r,file), SoundLoader.load(os.path.join(r,file))])
		if count == 1:
			Logger.info('Preload : one Soundfile loaded to memory')
		else:
			Logger.info('Preload : ' + str(count) + ' Soundfiles loaded to memory')

	def PreloadEDAssets(self):
		#preload Elite Dangerous Assets
		count = 0
		for r,d,f in os.walk("img\edassets"):
			for file in os.listdir(r):
				if file.endswith(".png"):
					count+=1
					print(os.path.join(r,file))
					self.preloadedAssets.append([file, Image(source=os.path.join(r,file)).texture])
		if count == 1:
			Logger.info('Preload : one ED-Asset Image loaded to memory as textures')
		else:
			Logger.info('Preload : ' + str(count) + ' ED-Assets Image loaded to memory as textures')
			
	def _PreloadEDAssets_Thread(self, instance):
		#preload Elite Dangerous Assets
		count = 0
		for r,d,f in os.walk("img\edassets"):
			for file in os.listdir(r):
				if file.endswith(".png"):
					count+=1
					instance.preloadedAssets.append([file, Image(source=os.path.join(r,file)).texture])
		if count == 1:
			Logger.info('Preload : one ED-Asset Image loaded to memory as textures')
		else:
			Logger.info('Preload : ' + str(count) + ' ED-Assets Image loaded to memory as textures')

	def PreloadEDAssets_Thread(self, instance):
		threading.Thread(target=lambda:self._PreloadEDAssets_Thread(instance)).start()

	def returnPreloadedAsset(self, AssetName):
		for x in self.preloadedAssets:
			if AssetName in x[0]:
				return x[1]