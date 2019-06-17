from kivy.logger import Logger

class Sounds():
	def PlayRndSound(self, preloadClass, configClass):
		rndlist = []
		count = 0
		for x in preloadedAssets:
			if 'clicks' in x[0]:
				count+=1
				rndlist.append(x[0])
		rndint = random.randint(0,count-1)
		x = preloadClass.returnPreloadedAsset(rndlist[rndint])
		if x != None:
			x.seek(0)
			x.volume = float(configClass.volume / 100)
			x.play()
		else:
			Logger.error('Sound : File 404')

	def PlayClickSound(preloadClass, configClass):
		x = preloadClass.returnPreloadedAsset('207.wav')
		if x != None:
			x.seek(0)
			x.volume = float(configClass.volume / 100)
			x.play()
		else:
			Logger.error('Sound : File 404')

	def PlaySound(preloadClass, configClass, soundFileName):
		x = preloadClass.returnPreloadedAsset(soundFileName)
		if x != None:
			x.seek(0)
			x.volume = float(configClass.volume / 100)
			x.play()
		else:
			Logger.error('Sound : File 404')
