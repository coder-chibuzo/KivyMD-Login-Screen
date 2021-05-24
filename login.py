#By Coder_Chibuzo

from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'



from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Brown"
		return Builder.load_file('login.kv')
	def logger(self):
		self.root.ids.welcome_label.text = f'Welcome {self.root.ids.user.text}!'

	def clear(self):
		self.root.ids.welcome_label.text = "WELCOME"		
		self.root.ids.user.text = ""		
		self.root.ids.password.text = ""		
	
MainApp().run()
