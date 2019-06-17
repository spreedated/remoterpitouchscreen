import os
import sys
import configparser
from kivy.logger import Logger
from cryptography.fernet import Fernet

class Configuration():
	#main
	socket = 'udp'
	socketfile = 'client_udp.py'
	sleepBetweenKeySends = 0.1
	pythonExecuteBinary = 'python'
	serverIPv4addr = ''
	serverIPv4port = 15548
	debug = False
	#sound
	volume = 100
	clicksounds = 1
	additionalSounds = 1
	#inara
	inara_username = ''
	inara_password = b''
	inara_apikey = ''
	inara_pass_key = b''
	#preload
	edassets = False
	#ship preload
	button0_label=''
	button0_key=''
	button1_label=''
	button1_key=''
	button2_label=''
	button2_key=''
	button3_label=''
	button3_key=''
	button4_label=''
	button4_key=''
	button5_label=''
	button5_key=''
	button6_label=''
	button6_key=''
	button7_label=''
	button7_key=''
	button8_label=''
	button8_key=''
	button9_label=''
	button9_key=''
	button10_label=''
	button10_key=''
	button11_label=''
	button11_key=''
	button12_label=''
	button12_key=''
	button13_label=''
	button13_key=''
	button14_label=''
	button14_key=''

	confFilePath = os.getcwd() + '/config.conf'
	keyFilePath = os.getcwd() + '/key'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if os.path.isfile(self.confFilePath):
			try:
				config = configparser.ConfigParser()
				config.read(self.confFilePath)
				#Set Config Vars
				#sound
				self.volume = int(config.get('SOUND','volume'))
				self.clicksounds = int(config.get('SOUND','clicksounds'))
				self.additionalSounds = int(config.get('SOUND','additionalSounds'))
				#main
				self.socket = str(config.get('MAIN','socket'))
				acc = str(config.get('MAIN','debug'))
				if acc == '1':
					self.debug = True
				if self.socket == 'tcp':
					self.socketfile = 'client_tcp.py'
				if self.socket == 'udp':
					self.socketfile = 'client_udp.py'
				self.sleepBetweenKeySends = float(config.get('MAIN','sleepBetweenKeySends'))
				self.pythonExecuteBinary = str(config.get('MAIN','pythonExecuteBinary'))
				self.serverIPv4addr = str(config.get('MAIN','serverIPv4addr'))
				self.serverIPv4port = int(config.get('MAIN','serverIPv4port'))
				#inara
				self.inara_username = str(config.get('INARA','username'))
				self.inara_password = str(config.get('INARA','password')).encode() #Converting to byte
				self.inara_apikey = str(config.get('INARA','apikey'))
				acc = str(config.get('PRELOAD','edassets'))
				if acc == '1':
					self.edassets = True
				#ship controls
				self.button0_label = str(config.get('SHIPCONTROLS','button0_label'))
				self.button0_key = str(config.get('SHIPCONTROLS','button0_key'))
				self.button1_label = str(config.get('SHIPCONTROLS','button1_label'))
				self.button1_key = str(config.get('SHIPCONTROLS','button1_key'))
				self.button2_label = str(config.get('SHIPCONTROLS','button2_label'))
				self.button2_key = str(config.get('SHIPCONTROLS','button2_key'))
				self.button3_label = str(config.get('SHIPCONTROLS','button3_label'))
				self.button3_key = str(config.get('SHIPCONTROLS','button3_key'))
				self.button4_label = str(config.get('SHIPCONTROLS','button4_label'))
				self.button4_key = str(config.get('SHIPCONTROLS','button4_key'))
				self.button5_label = str(config.get('SHIPCONTROLS','button5_label'))
				self.button5_key = str(config.get('SHIPCONTROLS','button5_key'))
				self.button6_label = str(config.get('SHIPCONTROLS','button6_label'))
				self.button6_key = str(config.get('SHIPCONTROLS','button6_key'))
				self.button7_label = str(config.get('SHIPCONTROLS','button7_label'))
				self.button7_key = str(config.get('SHIPCONTROLS','button7_key'))
				self.button8_label = str(config.get('SHIPCONTROLS','button8_label'))
				self.button8_key = str(config.get('SHIPCONTROLS','button8_key'))
				self.button9_label = str(config.get('SHIPCONTROLS','button9_label'))
				self.button9_key = str(config.get('SHIPCONTROLS','button9_key'))
				self.button10_label = str(config.get('SHIPCONTROLS','button10_label'))
				self.button10_key = str(config.get('SHIPCONTROLS','button10_key'))
				self.button11_label = str(config.get('SHIPCONTROLS','button11_label'))
				self.button11_key = str(config.get('SHIPCONTROLS','button11_key'))
				self.button12_label = str(config.get('SHIPCONTROLS','button12_label'))
				self.button12_key = str(config.get('SHIPCONTROLS','button12_key'))
				self.button13_label = str(config.get('SHIPCONTROLS','button13_label'))
				self.button13_key = str(config.get('SHIPCONTROLS','button13_key'))
				self.button14_label = str(config.get('SHIPCONTROLS','button14_label'))
				self.button14_key = str(config.get('SHIPCONTROLS','button14_key'))
				# ###
				Logger.info('Configuration : Loaded sucessfully')

				# Read/Create Key file to decrypt/encrypt password
				if(os.path.isfile(self.keyFilePath)):
					f = open(self.keyFilePath,'r')
					self.inara_pass_key = f.readline().encode() # Convert string to byte (IMPORTANT)
					f.close()
					Logger.info('Configuration : Using existing Keyfile')
				else:
					acc = Fernet.generate_key().decode('utf-8')
					f = open(self.keyFilePath,'w')
					f.write(acc)
					f.close()
					self.inara_pass_key = acc.encode()
					Logger.info('Configuration : Keyfile generated')
				# ###
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
				f.write('sleepBetweenKeySends=0.1\n')
				f.write('pythonExecuteBinary=python\n')
				f.write('serverIPv4addr=\n')
				f.write('serverIPv4port=15548\n')
				f.write('\n[PRELOAD]\n')
				f.write('edassets=0\n')
				f.write('\n[SOUND]\n')
				f.write('volume=100\n')
				f.write('clicksounds=1\n')
				f.write('additionalSounds=1\n')
				f.write('\n[INARA]\n')
				f.write('username=\n')
				f.write('password=\n')
				f.write('apikey=\n')
				f.write('\n;Key Bindings\n')
				f.write('[SHIPCONTROLS]\n')
				f.write('button0_label=\n')
				f.write('button0_key=\n')
				f.write('button1_label=\n')
				f.write('button1_key=\n')
				f.write('button2_label=\n')
				f.write('button2_key=\n')
				f.write('button3_label=\n')
				f.write('button3_key=\n')
				f.write('button4_label=\n')
				f.write('button4_key=\n')
				f.write('button5_label=\n')
				f.write('button5_key=\n')
				f.write('button6_label=\n')
				f.write('button6_key=\n')
				f.write('button7_label=\n')
				f.write('button7_key=\n')
				f.write('button8_label=\n')
				f.write('button8_key=\n')
				f.write('button9_label=\n')
				f.write('button9_key=\n')
				f.write('button10_label=\n')
				f.write('button10_key=\n')
				f.write('button11_label=\n')
				f.write('button11_key=\n')
				f.write('button12_label=\n')
				f.write('button12_key=\n')
				f.write('button13_label=\n')
				f.write('button13_key=\n')
				f.write('button14_label=\n')
				f.write('button14_key=\n')

				f.close()
			Logger.info('Configuration : Created successfully - Please adjust configuration and restart the app :)')
		except Exception:
		    Logger.critical('Configuration : Cannot create config file')
		finally:
			sys.exit(0)
