#!/usr/bin/env python

from urllib.request import urlopen
import json
#import matplotlib
#import matplotlib.pyplot as plt
import datetime
#import dateutil.parser
#import numpy

uppsalaStationCode = 97510
myLat = 59.836557
myLong = 17.606889

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.
	
    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

#def create24hForecastPlot(fcstData):
#	timeStamps = []
#	temps = []
#	for i in fcstData["timeSeries"]:
#		timeStamps.append(dateutil.parser.parse(i["validTime"]))
#		for j in i["parameters"]:
#			if j["name"]=="t":
#				temps.append(j["values"][0])

#	fig, ax = plt.subplots()
#	fig.autofmt_xdate()

#	timeStamps24h = timeStamps[0:44]
#	temps24h = temps[0:44]

#	ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1/4))
#	ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a %H:00'))

#	#plt.xlabel("Datum")
#	plt.ylabel("Temperatur (Prognos)")
#	plt.title("SMHI-prognos för temperatur")

#	ax.plot_date(timeStamps24h, temps24h, "-")#, marker = ".")
#	#ax.plot_date(timeStamps, yfit, "-")

#	plt.tick_params(which='major', length=6,width=1)
#	plt.tick_params(which='minor', length=3,width=1)
 
#	plt.gcf().subplots_adjust(bottom=0.25)
#	plt.xlim(timeStamps24h[0],timeStamps24h[-1])
#	plt.savefig("24hplot.png")

#def create10dayForecastPlot(fcstData):
#	timeStamps = []
#	temps = []
#	for i in fcstData["timeSeries"]:
#		timeStamps.append(dateutil.parser.parse(i["validTime"]))
#		for j in i["parameters"]:
#			if j["name"]=="t":
#				temps.append(j["values"][0])

#	fig, ax = plt.subplots()
#	fig.autofmt_xdate()

#	ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1/4))
#	ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a %d %b'))

#	#plt.xlabel("Datum")
#	plt.ylabel("Temperatur (Prognos)")
#	plt.title("SMHI-prognos för temperatur")

#	ax.plot_date(timeStamps, temps, " ", marker = ".")
#	#ax.plot_date(timeStamps, yfit, "-")

#	plt.tick_params(which='major', length=6,width=1)
#	plt.tick_params(which='minor', length=3,width=1)

#	plt.gcf().subplots_adjust(bottom=0.25)
#	plt.xlim(timeStamps[0],timeStamps[-1])
#	plt.savefig("10dayplot.png")

def setUrl(data):
	url = "https://opendata-download-metobs.smhi.se/api/version/{urlData[version]}/parameter/{urlData[parameter]}/station/{urlData[station]}/period/{urlData[period]}/data.json".format(urlData=data)
	return url

def printWithIndex(list):
	for i in range(0, len(list)-1):
		print((i, list))

def printWeatherData(data):
	print(
"""Lufttemperatur: {d[temperature]} \u00b0C
Vindhastighet: {d[wind]} m/s
Barometertryck: {d[pressure]} hPa
Luftfuktighet: {d[humidity]} %
Effektiv temperatur: {d[effectiveTemperature]} \u00b0C 
Mätningar gjorda {d[date]}""".format(d=data))

def getUppsalaData(parameter,stationCode=uppsalaStationCode):
	urlData ={
			"version":"latest",
			"parameter":parameter, 
			"station":stationCode,
			"period":"latest-hour"}
	return get_jsonparsed_data(setUrl(urlData))

def effectiveTemperature(temp,wind):
	if wind < 0.5:
		return temp
	else:
		return int(13.126667 + 0.6215*temp - 13.924748*(wind**0.16) + 0.4875195*temp*(wind**0.16))

def getCurrentWeather():
	#airtemperature and date
	data = getUppsalaData(1)
	temp = float(data["value"][0]["value"])
	date = data["value"][0]["date"]
	humanDate = datetime.datetime.fromtimestamp(date/1000)

	#windspeed
	data = getUppsalaData(4)
	wind = float(data["value"][0]["value"])

	#humidity
	data = getUppsalaData(6)
	humi = float(data["value"][0]["value"])

	#precipitation over last hour
	#data = getUppsalaData(7)
	#prec = float(data["value"][0]["value"])

	#snow depth measured at 6:00
	#data = getUppsalaData(8)
	#snow = float(data["value"][0]["value"])

	#pressure, at sealevel (i think)
	data = getUppsalaData(9)
	pres = float(data["value"][0]["value"])

	#sunshine time last hour
	#data = getUppsalaData(10)
	#sunt = float(data["value"][0]["value"])

	#sight range (11 is irradiance)
	#data = getUppsalaData(12)
	#sran = float(data["value"][0]["value"])

	#weather, coded as a three digit int
	data = getUppsalaData(13)
	summ = float(data["value"][0]["value"])

	effectiveTemp = effectiveTemperature(temp, wind)

	weatherData = {"temperature":temp,
				   "wind":wind,
				   "humidity":humi,
				   "weather":summ,
				   "pressure":pres,
				   #"precipitation":prec,
				   "effectiveTemperature":effectiveTemp,
				   "date":humanDate
				   }

	return weatherData

def plotLatLong():
	urlAllStations = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/4.json"
	dataAllStations = get_jsonparsed_data(urlAllStations)
	points = dataAllStations["station"]

	lat = [i["latitude"] for i in points]
	long = [i["longitude"] for i in points]

	plt.ylabel("latitud")
	plt.xlabel("longitud")

	plt.scatter(long,lat)

	plt.show()

uppsalaStationCode = 97510
myLat = 59.836557
myLong = 17.606889

#printWeatherData(getCurrentWeather())

#url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{}/lat/{}/data.json".format(myLong,myLat)

#data = get_jsonparsed_data(url)

#with open("fcstdata.json", "w") as fcst_data_file:
#    json.dump(data, fcst_data_file, indent=4)
#plotLatLong()
#create24hForecastPlot(data)
#create10dayForecastPlot(data)


