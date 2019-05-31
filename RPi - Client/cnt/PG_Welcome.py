from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from kivy.lang import Builder

Builder.load_string("""
<PG_Welcome>:
	LCARS_Label:
		text: 'PRIMARY SYSTEMS TERMINAL'
		pos: 118,349
		size: 665,46
	LCARS_Label:
		text: 'ACCESS GRANTED'
		pos: 118,88
		size: 665,46
	Image:
		pos: 118,176
		size: 665,133
		size_hint: None,None
		id: img_Logo
""")

class PG_Welcome(FloatLayout):
	id='PG_Welcome'

	def __init__(self, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.ids['img_Logo'].texture = preloadClass.returnPreloadedAsset('logo.png')

		if configClass.debug:
			Logger.info('Page_Welcome : Loaded!')
