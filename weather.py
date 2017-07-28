import kivy
kivy.require('1.10.0')

from kivy.app import App 
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout

class WeatherApp(App):

	def build(self):
		return FloatLayout()

if __name__ == "__main__":
	weather_kivy = WeatherApp()
	weather_kivy.run()