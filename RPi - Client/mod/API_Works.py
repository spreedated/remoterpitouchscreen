import urllib3
import json
import requests
import datetime
from kivy.logger import Logger
import mod.Information as ApplicationInfo

class API_Inara():
	configClass = None
	infoClass = None

	SESSION = requests.session()

	errormsg = None

	apikey = None

	def __init__(self, configClass, infoClass, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.configClass = configClass
		self.infoClass = infoClass

		apikey = configClass.inara_apikey
		#read apikey
		if len(apikey) <= 6:
			Logger.critical('API Inara : No API Key')
			self.errormsg = 'No API Key'
			return
		self.apikey = apikey
		#self.GetCmdrName()
		self.GetCMDRProfile()

		if configClass.debug:
			Logger.info('API Inara : Retrieved info from INARA.CZ')

	def GetCMDRProfile(self):
		payload = { "header": self._api_header(), "events" : [self._api_cmdrprofile()] }
		resp = self.SESSION.post('https://inara.cz/inapi/v1/', json=payload)
		json_resp = json.loads(resp.content.decode('utf-8'))

		if json_resp['header']['eventStatus'] != requests.codes.ok:
			Logger.critical('API Inara : ' + str(json_resp['header']['eventStatusText']))
			self.errormsg = str(json_resp['header']['eventStatusText'])
			return
		else:
			#Get CMDR Ranks
			for element in json_resp['events'][0]['eventData']['commanderRanksPilot']:
				if element['rankName'] == 'combat':
					self.infoClass.cmdr_combatrank = ApplicationInfo.CombatRanks[element['rankValue']]
				if element['rankName'] == 'trade':
					self.infoClass.cmdr_traderank = ApplicationInfo.TradeRanks[element['rankValue']]
				if element['rankName'] == 'exploration':
					self.infoClass.cmdr_explorationrank = ApplicationInfo.ExplorationRanks[element['rankValue']]
				if element['rankName'] == 'cqc':
					self.infoClass.cmdr_cqcrank = ApplicationInfo.CQCRanks[element['rankValue']]
			#Get CMDR Name
			self.infoClass.cmdr_name = json_resp['header']['eventData']['userName']
			Logger.info('API Inara : CMDR Name retrieved ['+self.infoClass.cmdr_name+']')

			squad = json_resp['events'][0]['eventData']['commanderSquadron']['squadronName']
			if squad != None:
				self.infoClass.cmdr_squadron = squad

	def GetCmdrName(self):
		payload = { "header": self._api_header() }
		resp = self.SESSION.post('https://inara.cz/inapi/v1/', json=payload)
		json_resp = json.loads(resp.content.decode('utf-8'))

		if json_resp['header']['eventStatus'] != requests.codes.ok:
			Logger.critical('API Inara : ' + str(json_resp['header']['eventStatusText']))
			self.errormsg = str(json_resp['header']['eventStatusText'])
			return
		else:
			self.infoClass.cmdr_name = json_resp['header']['eventData']['userName']
			Logger.info('API Inara : CMDR Name retrieved ['+self.infoClass.cmdr_name+']')

	def _api_header(self):
		if self.infoClass.cmdr_name != None:
			return {
				'appName': 'E:D RPi-Companion',
				'appVersion': '1.0',
				'isDeveloped': self.configClass.debug,
				'APIkey': self.apikey,
				'commanderName': self.infoClass.cmdr_name
				}
		else:
			return {
				'appName': 'E:D RPi-Companion',
				'appVersion': '1.0',
				'isDeveloped': self.configClass.debug,
				'APIkey': self.apikey
				}

	def _api_cmdrprofile(self):
		return {
			"eventName": "getCommanderProfile",
			"eventTimestamp": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
				"eventData": {
				"searchName": self.infoClass.cmdr_name
				}
			}
