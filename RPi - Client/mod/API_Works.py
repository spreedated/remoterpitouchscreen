import urllib3
import json
import requests
import datetime
from kivy.logger import Logger

class Inara():
	SESSION = requests.session()
	CombatRanks = ['Harmless','Mostly Harmless','Novice','Competent','Expert','Master','Dangerous','Deadly','Elite']
	TradeRanks = ['Penniless','Mostly Penniless','Peddler','Dealer','Merchant','Broker','Entrepreneur','Tycoon','Elite']
	ExplorationRanks = ['Aimless','Mostly Aimless','Scout','Surveyor','Trailblazer','Pathfinder','Ranger','Pioneer','Elite']
	CQCRanks = ['Helpless','Mostly Helpless','Amateur','Semi Professional','Professional','Champion','Hero','Legend','Elite']

	state = True

	apikey = None
	cmdr_name = None
	cmdr_combatrank = None
	cmdr_traderank = None
	cmdr_explorationrank = None
	cmdr_cqcrank = None
	cmdr_squadron = None

	def __init__(self, configClass, *args, **kwargs):
		super().__init__(*args, **kwargs)

		apikey = configClass.inara_apikey
		#read apikey
		if len(apikey) <= 6:
			Logger.critical('API Inara : No API Key')
			self.state = False
			return
		self.apikey = apikey
		self.GetCmdrName()
		self.GetCMDRProfile()

	def GetCMDRProfile(self):
		payload = { "header": self._api_header(), "events" : [self._api_cmdrprofile()] }
		resp = self.SESSION.post('https://inara.cz/inapi/v1/', json=payload)
		json_resp = json.loads(resp.content)

		if json_resp['header']['eventStatus'] != requests.codes.ok:
			Logger.critical('API Inara : ' + str(json_resp['header']['eventStatusText']))
			self.state = False
		else:
			for element in json_resp['events'][0]['eventData']['commanderRanksPilot']:
				if element['rankName'] == 'combat':
					self.cmdr_combatrank = self.CombatRanks[element['rankValue']]
				if element['rankName'] == 'trade':
					self.cmdr_traderank = self.TradeRanks[element['rankValue']]
				if element['rankName'] == 'exploration':
					self.cmdr_explorationrank = self.ExplorationRanks[element['rankValue']]
				if element['rankName'] == 'cqc':
					self.cmdr_cqcrank = self.CQCRanks[element['rankValue']]

			squad = json_resp['events'][0]['eventData']['commanderSquadron']['squadronName']
			if squad != None:
				self.cmdr_squadron = squad

	def GetCmdrName(self):
		payload = { "header": self._api_header() }
		resp = self.SESSION.post('https://inara.cz/inapi/v1/', json=payload)
		json_resp = json.loads(resp.content)

		if json_resp['header']['eventStatus'] != requests.codes.ok:
			Logger.critical('API Inara : ' + str(json_resp['header']['eventStatusText']))
			self.state = False
		else:
			self.cmdr_name = json_resp['header']['eventData']['userName']
			Logger.info('API Inara : CMDR Name retrieved ['+self.cmdr_name+']')

	def _api_header(self):
		if self.cmdr_name != None:
			return {
				'appName': 'EDRecon',
				'appVersion': '1.0',
				'isDeveloped': True,
				'APIkey': self.apikey,
				'commanderName': self.cmdr_name
				}	
		else:
			return {
				'appName': 'EDRecon',
				'appVersion': '1.0',
				'isDeveloped': True,
				'APIkey': self.apikey
				}

	def _api_cmdrprofile(self):
		return {
			"eventName": "getCommanderProfile",
			"eventTimestamp": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
				"eventData": {
				"searchName": self.cmdr_name
				}
			}
