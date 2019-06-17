import os
import time
from subprocess import Popen, PIPE
from kivy.logger import Logger

class ServerEngine(object):

	def sendKeys(configClass, sequence, type='key'):
		try:
			for key in sequence:
				p = Popen([configClass.pythonExecuteBinary, os.path.join(os.getcwd(), 'fnc', configClass.socketfile), type, key], stdout=PIPE, stderr=PIPE)
				stdout, stderr = p.communicate()

				if configClass.debug and len(stdout.decode('UTF-8')) >= 1:
					Logger.info('ServerEngine[sendKeys]:' + stdout.decode('UTF-8').replace('\n',''))
					Logger.info('ServerEngine[sendKeys]: KeySent: ' + key)

				if configClass.debug and len(stderr) >= 1:
					Logger.error('ServerEngine[sendKeys]:' + stderr)

				time.sleep(configClass.sleepBetweenKeySends)
		except Exception as e:
		    Logger.fatal('ServerEngine[sendKeys]:' + str(e))
		