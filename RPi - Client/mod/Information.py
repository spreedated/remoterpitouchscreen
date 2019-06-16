appname = 'E:D RPi Companion'
version = 'v0.2.1'
appFullName =  appname + ' ' + version


CombatRanks = [('Harmless','combat_rank0.png'),('Mostly Harmless','combat_rank1.png'),('Novice','combat_rank2.png'),('Competent','combat_rank3.png'),('Expert','combat_rank4.png'),('Master','combat_rank5.png'),('Dangerous','combat_rank6.png'),('Deadly','combat_rank7.png'),('Elite','combat_rank8.png')]
TradeRanks = [('Penniless','trade_rank0.png'),('Mostly Penniless','trade_rank1.png'),('Peddler','trade_rank2.png'),('Dealer','trade_rank3.png'),('Merchant','trade_rank4.png'),('Broker','trade_rank5.png'),('Entrepreneur','trade_rank6.png'),('Tycoon','trade_rank7.png'),('Elite','combat_rank8.png')]
ExplorationRanks = [('Aimless','explorer_rank0.png'),('Mostly Aimless','explorer_rank1.png'),('Scout','explorer_rank2.png'),('Surveyor','explorer_rank3.png'),('Trailblazer','explorer_rank4.png'),('Pathfinder','explorer_rank5.png'),('Ranger','explorer_rank6.png'),('Pioneer','explorer_rank7.png'),('Elite','explorer_rank8.png')]
CQCRanks = [('Helpless','cqc_rank0.png'),('Mostly Helpless','cqc_rank1.png'),('Amateur','cqc_rank2.png'),('Semi Professional','cqc_rank3.png'),('Professional','cqc_rank4.png'),('Champion','cqc_rank5.png'),('Hero','cqc_rank6.png'),('Legend','cqc_rank7.png'),('Elite','cqc_rank8.png')]

class DynamicInformation():

	cmdr_name = None
	cmdr_combatrank = None
	cmdr_traderank = None
	cmdr_explorationrank = None
	cmdr_cqcrank = None
	cmdr_squadron = None

	def __init__(self, *args, **kwargs):
		return super().__init__(*args, **kwargs)


