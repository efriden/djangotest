from django.conf import settings
from dashing.widgets import NumberWidget
import TestApp.weather as w

class Weather(NumberWidget):
	title = "Uppsala"
	def get_value(self):
		return "34"
		weatherData = w.getCurrentWeather()
		print (weatherData)
		return weatherData["temperature"]