import requests
import lxml.html
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from scrapy.selector import Selector
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.logger import Logger
from mod.Color import ColorConversion

Builder.load_string("""
<PG_Inara_Fleet>:
	stacky: stacky
	size_hint: None,None
	size: 665,383
	pos: 118,49
	BoxLayout:
		pos: 0,0
		size: 665,0
		size_hint: None,None
		spacing: 10
		orientation: 'vertical'
		id: stacky
""")

class PG_Inara_Fleet(ScrollView):
	id='PG_Inara_Fleet'
	stacky = ObjectProperty()

	fleetdetails = [] # [0]name - [1]id - [2]type - [3]value_str - [4]value_int - [5]dock - [6]linktodetails
	fleetcount = 0
	fleetvalue = 0
	status = None # If everything went okay

	def __init__(self, configInstance, preloadClass, infoClass, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.Inara_ProcessFleet(self.Inara_GetFleet(configInstance))

		stacky_y = 0
		for ship in self.fleetdetails:
			print(ship)
			col = ColorConversion.RGBA_to_Float(0,168,89)
			x = Label(size=(640,177))
			with x.canvas.after:
				Color(col[0],col[1],col[2],col[3])
				RoundedRectangle(pos=x.pos, size=x.size, radius=(42,42,42,42))
			self.stacky.add_widget(x)
			stacky_y += (x.size[1] + 10)

		self.stacky.size = (self.stacky.size[0], stacky_y)

		Logger.info('PageFunction : Pageswitch - PG_Inara_Fleet')

	# Back-End
	def Inara_GetFleet(self, configinstance):
		session = self.cas_login(configinstance.inara_username, configinstance.inara_password)
		if session == 'timeout':
			return 'timeout'
		try:
		    res = session.get('https://inara.cz/cmdr-fleet/', timeout=5)
		except Exception as e:
		    return 'timeout'
		return res.text

	def cas_login(self, username, password, service=''):
		# GET parameters - URL we'd like to log into.
		params = {'service': service}
		LOGIN_URL = 'https://inara.cz/login/'

		# Start session and get login form.
		session = requests.session()
		try:
			login = session.get(LOGIN_URL, params=params, timeout=5)
		except Exception as e:
			return 'timeout'
		
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
			self.status = 'No Login'
			return
		elif 'timeout' in rawHTML: 
			self.status = 'Inara Timeout'
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
