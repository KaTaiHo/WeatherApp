import kivy
import requests
import json
kivy.require('1.10.0')

from kivy.app import App 
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.size = (400, 700)


class WeatherFloatLayout(FloatLayout):
	
	data = {}
	current_description = StringProperty()
	temp = 0.0

	def __init__(self, **kwargs):
		super(WeatherFloatLayout, self).__init__(**kwargs)
		self.data = ''

	def get_weather_data(self):
		print ('data pressed')
		api_key = '28d0ca9a9aff408aa4f90c51689be4ed'
		r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=78751,us&appid=' + api_key)
		self.data = json.loads(r.text)
		self.current_description = self.data['weather'][0]['description']
		self.temp = self.data['main']['temp']




class WeatherApp(App):

	def build(self):
		return WeatherFloatLayout()

if __name__ == "__main__":
	weather_kivy = WeatherApp()
	weather_kivy.run()