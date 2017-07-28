import kivy
kivy.require('1.10.0')

from kivy.app import App 
from kivy.uix.button import Label

class WeatherApp(App):

	def build(self):
		return Label()

if __name__ == "__main__":
	weather_kivy = WeatherApp()
	weather_kivy.run()