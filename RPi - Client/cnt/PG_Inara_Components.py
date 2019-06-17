import requests
import lxml.html
import math
from cryptography.fernet import Fernet
from kivy.uix.button import Button
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
<PG_Inara_Components>:
	floaty: floaty
	size_hint: None,None
	size: 665,383
	pos: 118,49
	FloatLayout:
		pos: 0,0
		size: 665,300
		size_hint: None,None
		id: floaty
""")

class PG_Inara_Components(ScrollView):
	id='PG_Inara_Components'
	floaty = ObjectProperty()

	components = [] # [0]name - [1]have - [2]icon (13x13)
	
	status = None # If everything went okay

	def __init__(self, configInstance, preloadClass, infoClass, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		#Reset
		self.components = []
		status = None

		self.Inara_ProcessComponents(self.Inara_GetComponents(configInstance))

		if self.status != None:
			Logger.critical('Page Inara Components : ' + str(self.status))
			x = Label(size=(665,300), size_hint=(None,None), pos=(0,0), text=str(self.status), font_name='fnt/lcarsgtj3.ttf', font_size='72sp', id=self.id, halign='center', color=(0.99,0.61,0,1))
			self.floaty.add_widget(x)
			return

		#Build Floaty (FloatLayout inside ScrollView)
		self.components.sort(reverse=True)
		
		floaty_y = 0
		next_pos_x = 331 #Starting by building the right column first
		next_pos_y = 0
		halftime = int(math.ceil(len(self.components)/2)) #Calc when to break to next column, math.ceil for round UP

		for component in self.components:
			#print(ship)
			xSize = (330,30)
			xPos = (next_pos_x, next_pos_y)

			#Icon
			if component[2] != None:
				x_Icon = Image(source='img/matgrades/'+component[2], pos=(xPos[0]+10, xPos[1]+8), size=(13,13), size_hint=(None,None), id=self.id)
				self.floaty.add_widget(x_Icon)

			#Name
			x_Name = Label(text=component[0], markup=True, color=(1,1,1,0.8), pos=(xPos[0]+30, xPos[1]+1), size=(260,xSize[1]), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='20sp', id=self.id, halign='left', text_size=(260,xSize[1]), shorten_from='right', split_str=' ', shorten=True)
			self.floaty.add_widget(x_Name)

			#Have
			x_Have = Label(text=str(component[1]), markup=True, color=(1,1,1,1), pos=(xPos[0]+295, xPos[1]+1), size=(30,xSize[1]), size_hint=(None,None), font_name='fnt/lcarsgtj3.ttf', font_size='24sp', id=self.id, halign='right', text_size=(30,xSize[1]), shorten_from='right', split_str=' ', shorten=True)
			self.floaty.add_widget(x_Have)

			addup = xSize[1] + 1
			next_pos_y += addup

			#check when to switch to next column
			halftime -= 1
			if halftime == 0:
				next_pos_x = 0
				next_pos_y = 0
			elif halftime >= -1:
				floaty_y += (addup)
			
			#self.floaty.add_widget(x)

		#set size of floatlayout
		self.floaty.size = (self.floaty.size[0], (floaty_y))

		Logger.info('PageFunction : Pageswitch - PG_Inara_Components')

	# Back-End
	def Inara_GetComponents(self, configinstance):
		try:
		    unciphered = Fernet(configinstance.inara_pass_key).decrypt(configinstance.inara_password).decode("utf-8")
		except Exception as e:
		    return 'unciphererror'

		session = self.cas_login(configinstance.inara_username, unciphered)
		if session == 'timeout':
			return 'timeout'
		try:
		    res = session.get('https://inara.cz/cmdr-cargo/', timeout=5)
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

	def Inara_ProcessComponents(self, rawHTML):
		if 'Guest</a>' in rawHTML:
			self.status = 'No Login\nor wrong credentials'
			return
		elif 'timeout' in rawHTML: 
			self.status = 'Inara Timeout'
			return
		elif 'unciphererror' in rawHTML: 
			self.status = 'Error in unciphering\npassword - corrupt keyfile'
			return

		r = Selector(text=rawHTML).xpath("//div[@class='inventorymaterial ']").extract()

		for componentblock in r:
			component_Icon = componentblock[componentblock.find('matgrade')+8:]
			component_Icon = component_Icon[:component_Icon.find('"')]

			component_Name = componentblock[componentblock.find('<a')+1:]
			component_Name = component_Name[component_Name.find('>')+1:]
			component_Name = component_Name[:component_Name.find('<')]

			component_Have = componentblock[componentblock.find('havevalue'):]
			component_Have = component_Have[component_Have.find('>')+1:]
			component_Have = component_Have[:component_Have.find('<')]
			component_Have = int(component_Have)

			self.components.append((component_Name, component_Have, component_Icon))
