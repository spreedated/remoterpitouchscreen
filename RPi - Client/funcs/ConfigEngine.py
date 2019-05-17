import os
#Init Conffile
clicksounds=1

confFilePath = os.getcwd() + '/config.conf'
if os.path.isfile(confFilePath):
	try:
		config = configparser.ConfigParser()
		config.read(confFilePath)
		clicksounds = int(config.get('MAIN','clicksounds'))
		print('[+] conf loaded success...')
	except Exception as e :
		print(e)
		try:
			os.remove(confFilePath)
		except Exception as e:
			print(e)
else:
	with open(confFilePath, 'x') as f:
		f.write('[MAIN]\n')
		f.write('clicksounds=1\n')
		f.close()
