import requests
import lxml.html
from cryptography.fernet import Fernet
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
	floaty: floaty
	size_hint: None,None
	size: 665,383
	pos: 118,49
	FloatLayout:
		pos: 0,0
		size: 665,300
		size_hint: None,None
		spacing: 10
		orientation: 'vertical'
		id: floaty
""")

class PG_Inara_Fleet(ScrollView):
	id='PG_Inara_Fleet'
	floaty = ObjectProperty()

	fleetdetails = [] # [0]name - [1]id - [2]type - [3]value_str - [4]value_int - [5]dock - [6]linktodetails
	fleetcount = 0
	fleetvalue = 0
	status = None # If everything went okay

	def __init__(self, configInstance, preloadClass, infoClass, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		#Reset
		self.fleetdetails = []
		self.fleetcount = 0
		self.fleetvalue = 0
		status = None

		self.Inara_ProcessFleet(self.Inara_GetFleet(configInstance))

		if self.status != None:
			Logger.critical('Page Inara Fleet : ' + str(self.status))
			x = Label(size=(665,300), size_hint=(None,None), pos=(0,0), text=str(self.status), font_name='fnt/lcarsgtj3.ttf', font_size='72sp', id=self.id, halign='center', color=(0.99,0.61,0,1))
			self.floaty.add_widget(x)
			return

		#Build Floaty (FloatLayout inside ScrollView)
		self.fleetdetails.sort(reverse=True)
		
		floaty_y = 0
		next_pos_y = 0
		ships_images = [
			('Diamondback Explorer','dbx2.png'),
			('Adder','adder2.png'),
			('Anaconda','anaconda2.png'),
			('Asp Explorer','aspx2.png'),
			('Fer-De-Lance','fdl2.png'),
			('Hauler','hauler2.png'),
			('Imperial Clipper','imp_clipper2.png'),
			('Imperial Courier','imp_courier2.png'),
			('Imperial Cutter','imp_cutter2.png'),
			('Imperial Eagle','imp_eagle2.png'),
			('Keelback','keelback2.png'),
			('Orca','orca2.png'),
			('Python','python2.png'),
			('Sidewinder','side2.png'),
			('Type-6 Transporter','type62.png'),
			('Type-7 Transporter','type72.png'),
			('Type-9 Transporter','type92.png'),
			('Viper MK III','vipermk32.png'),
			('Viper MK IV','vipermk42.png'),
			('Vulture','vulture2.png'),
				  ]
		for ship in self.fleetdetails:
			#print(ship)
			x = Label(size=(640,177), size_hint=(None,None), pos=(0,next_pos_y))
			with x.canvas.after:
				Color(1,1,1,0.2)
				RoundedRectangle(pos=x.pos, size=x.size, radius=(42,42,42,42))
			
			#Name
			x_Name_LBL = Label(text='Name', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+148, x.pos[1]+160), size=(250,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(250,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Name_LBL)
			x_Name = Label(text=ship[0], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+146, x.pos[1]+127), size=(240,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(240,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Name)

			#ID
			x_ID_LBL = Label(text='ID', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+148, x.pos[1]+105), size=(250,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(250,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_ID_LBL)
			x_ID = Label(text=ship[1], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+146, x.pos[1]+72), size=(80,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(80,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_ID)

			#Type
			x_Type_LBL = Label(text=ship[2], markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+10, x.pos[1]+145), size=(130,20), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='center', text_size=(130,20), shorten_from='right', split_str=' ', shorten=True)
			#with x_Type_LBL.canvas.before:
			#	Color(1,1,1,1)
			#	Rectangle(pos=x_Type_LBL.pos, size=x_Type_LBL.size)
			x.add_widget(x_Type_LBL)

			#Value Cr
			x_Value_LBL = Label(text='Name', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+398, x.pos[1]+160), size=(230,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(230,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Value_LBL)
			x_Value = Label(text=ship[3], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+398, x.pos[1]+127), size=(230,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(230,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Value)

			#Dock
			x_Dock_LBL = Label(text='Current Dock', markup=True, color=(0.4,0.4,0.4,1), pos=(x.pos[0]+148, x.pos[1]+43), size=(100,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='18sp', id=self.id, halign='left', text_size=(100,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Dock_LBL)
			x_Dock = Label(text=ship[5], markup=True, color=(0.8,0.8,0.8,1), pos=(x.pos[0]+146, x.pos[1]+10), size=(480,33), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='36sp', id=self.id, halign='left', text_size=(480,50), shorten_from='right', split_str=' ', shorten=True)
			x.add_widget(x_Dock)

			#Picture
			img_string = None
			for xb in range(len(ships_images)):
				if str(ship[2]).lower() in str(ships_images[xb][0]).lower():
					img_string = ships_images[xb][1]

			if img_string != None:
				x_Picture = Image(source='img/edassets/ships/'+img_string,pos=(x.pos[0]+10, x.pos[1]+5), size=(125,142), size_hint=(None,None), id=self.id)
				x.add_widget(x_Picture)

			next_pos_y += 187
			self.floaty.add_widget(x)
			floaty_y += (x.size[1] + 10)
				

		#set size of floatlayout
		self.floaty.size = (self.floaty.size[0], floaty_y)

		Logger.info('PageFunction : Pageswitch - PG_Inara_Fleet')

	# Back-End
	def Inara_GetFleet(self, configinstance):
		try:
		    unciphered = Fernet(configinstance.inara_pass_key).decrypt(configinstance.inara_password).decode("utf-8")
		except Exception as e:
		    return 'unciphererror'
		
		session = self.cas_login(configinstance.inara_username, unciphered)
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
			self.status = 'No Login\nor wrong credentials'
			return
		elif 'timeout' in rawHTML: 
			self.status = 'Inara Timeout'
			return
		elif 'unciphererror' in rawHTML: 
			self.status = 'Error in unciphering\npassword - corrupt keyfile'
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
