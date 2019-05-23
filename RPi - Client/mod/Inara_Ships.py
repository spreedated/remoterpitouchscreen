import requests
import lxml.html
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

class Ships():
	fleetdetails = [] # [0]name - [1]id - [2]type - [3]value_str - [4]value_int - [5]dock - [6]linktodetails
	fleetcount = 0
	fleetvalue = 0
	status = True # If everything went okay

	def __init__(self, configinstance, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.Inara_ProcessFleet(self.Inara_GetFleet(configinstance))

	def Inara_GetFleet(self, configinstance):
		print(configinstance.inara_username)
		session = self.cas_login(configinstance.inara_username, configinstance.inara_password)
		res = session.get('https://inara.cz/cmdr-fleet/')
		
		return res.text

	def cas_login(self, username, password, service=''):
	    # GET parameters - URL we'd like to log into.
	    params = {'service': service}
	    LOGIN_URL = 'https://inara.cz/login/'

	    # Start session and get login form.
	    session = requests.session()
	    login = session.get(LOGIN_URL, params=params)

	    # Get the hidden elements and put them in our form.
	    login_html = lxml.html.fromstring(login.text)
	    hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
	    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

	    # "Fill out" the form.
	    form['loginid'] = username
	    form['loginpass'] = password

	    # Finally, login and return the session.
	    session.post(LOGIN_URL, data=form, params=params)
	    return session

	def Inara_ProcessFleet(self, rawHTML):
		if 'Guest</a>' in rawHTML:
			self.status = False
			return

		r = Selector(text=rawHTML).xpath("//div[@class='shipblockcontainer']").extract()

		for shipblock in r:
			shipname = Selector(text=shipblock).xpath("//span[@class='major']/text()").get()

			if shipname == None:
				shipname = 'Unnamed'

			shipid = shipblock[shipblock.find('ID:</span>'):]
			shipid = shipid[shipid.find('>')+1:]
			shipid = shipid[:shipid.find('<')]
			shipid = shipid.lstrip(' ')

			shiptype = shipblock[shipblock.find('Type:</span>'):]
			shiptype = shiptype[shiptype.find('>')+1:]
			shiptype = shiptype[:shiptype.find('<')]
			shiptype = shiptype.lstrip(' ')

			shipvalue = shipblock[shipblock.find('Value:</span>'):]
			shipvalue = shipvalue[shipvalue.find('>')+1:]
			shipvalue = shipvalue[:shipvalue.find('<')]
			shipvalue = shipvalue.lstrip(' ')

			shipvalue_int = shipvalue.replace(',','')
			shipvalue_int = shipvalue_int.replace('Cr','')
			shipvalue_int = shipvalue_int.replace(' ','')
			shipvalue_int = int(shipvalue_int)

			self.fleetvalue+=shipvalue_int

			if '>Current ship<' in shipblock:
				shipdock = 'Current Ship'
			else:
				shipdock = shipblock[shipblock.find('Dock:</span>'):]
				shipdock = shipdock[shipdock.find('>')+1:]
				shipdock = shipdock[shipdock.find('>')+1:]
				shipdock = shipdock[:shipdock.find('<')]
				shipdock = shipdock.lstrip(' ')

			shipdetaillink = shipblock[shipblock.find('/cmdr-fleet/'):]
			shipdetaillink = shipdetaillink[:shipdetaillink.find('"')]

			self.fleetdetails.append((shipname, shipid, shiptype, shipvalue, shipvalue_int, shipdock, shipdetaillink))
			self.fleetcount+=1

#x = Ships()

#print(x.fleetdetails[3][2])