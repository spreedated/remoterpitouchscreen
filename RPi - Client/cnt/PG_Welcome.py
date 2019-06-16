from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from kivy.lang import Builder
import mod.Information as ApplicationInfo

Builder.load_string("""
<PG_Welcome>:
	LCARS_Label:
		pos: 118,49
		size: 665,102
		text_size: 665,102
		halign: 'center'
		id: mainText
	Image:
		pos: 118,160
		size: 665,271
		size_hint: None,None
		id: img_Logo
""")

class PG_Welcome(FloatLayout):
	id='PG_Welcome'

	def __init__(self, configClass, preloadClass, **kwargs):
		super().__init__(**kwargs)

		self.ids['img_Logo'].texture = preloadClass.returnPreloadedAsset('logo.png')
		self.ids['mainText'].text = ApplicationInfo.appFullName

		if configClass.debug:
			Logger.info('Page_Welcome : Loaded!')
