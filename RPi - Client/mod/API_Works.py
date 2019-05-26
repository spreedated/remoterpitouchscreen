import urllib3
import json
import requests
import datetime
from kivy.logger import Logger

class API_Inara():
	SESSION = requests.session()
	CombatRanks = [('Harmless','combat_rank0.png'),('Mostly Harmless','combat_rank1.png'),('Novice','combat_rank2.png'),('Competent','combat_rank3.png'),('Expert','combat_rank4.png'),('Master','combat_rank5.png'),('Dangerous','combat_rank6.png'),('Deadly','combat_rank7.png'),('Elite','combat_rank8.png')]
	TradeRanks = [('Penniless','trade_rank0.png'),('Mostly Penniless','trade_rank1.png'),('Peddler','trade_rank2.png'),('Dealer','trade_rank3.png'),('Merchant','trade_rank4.png'),('Broker','trade_rank5.png'),('Entrepreneur','trade_rank6.png'),('Tycoon','trade_rank7.png'),('Elite','combat_rank8.png')]
	ExplorationRanks = [('Aimless','explorer_rank0.png'),('Mostly Aimless','explorer_rank1.png'),('Scout','explorer_rank2.png'),('Surveyor','explorer_rank3.png'),('Trailblazer','explorer_rank4.png'),('Pathfinder','explorer_rank5.png'),('Ranger','explorer_rank6.png'),('Pioneer','explorer_rank7.png'),('Elite','explorer_rank8.png')]
	CQCRanks = [('Helpless','cqc_rank0.png'),('Mostly Helpless','cqc_rank1.png'),('Amateur','cqc_rank2.png'),('Semi Professional','cqc_rank3.png'),('Professional','cqc_rank4.png'),('Champion','cqc_rank5.png'),('Hero','cqc_rank6.png'),('Legend','cqc_rank7.png'),('Elite','cqc_rank8.png')]

	errormsg = None

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
			self.errormsg = 'No API Key'
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
			self.errormsg = str(json_resp['header']['eventStatusText'])
			return
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
			self.errormsg = str(json_resp['header']['eventStatusText'])
			return
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
