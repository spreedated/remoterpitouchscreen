import os
import sys
import configparser
from kivy.logger import Logger

class Configuration():
	#main
	socket = 'udp'
	socketfile = 'client_udp.py'
	debug = False
	#sound
	clicksounds = 1
	#inara
	inara_username = ''
	inara_password = ''
	inara_apikey = ''
	#preload
	edassets = False

	confFilePath = os.getcwd() + '/config.conf'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if os.path.isfile(self.confFilePath):
			try:
				config = configparser.ConfigParser()
				config.read(self.confFilePath)
				#Set Config Vars
				self.clicksounds = int(config.get('SOUND','clicksounds'))
				self.socket = str(config.get('MAIN','socket'))
				acc = str(config.get('MAIN','debug'))
				if acc == '1':
					self.debug = True
				if self.socket == 'tcp':
					self.socketfile = 'client_tcp.py'
				if self.socket == 'udp':
					self.socketfile = 'client_udp.py'
				self.inara_username = str(config.get('INARA','username'))
				self.inara_password = str(config.get('INARA','password'))
				self.inara_apikey = str(config.get('INARA','apikey'))
				acc = str(config.get('PRELOAD','edassets'))
				if acc == '1':
					self.edassets = True
				# ###
				Logger.info('Configuration : Loaded sucessfully')
			except Exception as e :
				Logger.info('Configuration : ' + str(e))
				try:
					os.remove(self.confFilePath)
					self.CreateConfig()
				except Exception as e:
					Logger.info('Configuration : ' + str(e))
		else:
			self.CreateConfig()	

	def CreateConfig(self):
		try:
			with open(self.confFilePath, 'x') as f:
				f.write('[MAIN]\n')
				f.write('socket=udp\n')
				f.write('debug=0\n')
				f.write('\n[PRELOAD]\n')
				f.write('edassets=0\n')
				f.write('\n[SOUND]\n')
				f.write('clicksounds=1\n')
				f.write('\n[INARA]\n')
				f.write('username=\n')
				f.write('password=\n')
				f.write('apikey=\n')
				f.close()
			Logger.info('Configuration : Created successfully - Please adjust configuration and restart the app :)')
		except Exception:
		    Logger.critical('Configuration : Cannot create config file')
		finally:
			sys.exit(0)
