import requests
import json

apikey = "61d22ef537895399c7752506c14a0514"

cities = ["Tokyo,JP", "London,UK", "New York,US"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

k2c = lambda k: k - 273.15

for name in cities:
	# get api url
	url = api.format(city=name, key=apikey)
	r = requests.get(url)
	#result is JSON, that't why decode.
	data = json.loads(r.text)
	print(data)
	# print results
	print("+ city=", data["name"])
	print("| weather=", data["weather"][0]["description"])
	print("| low temperature=", k2c(data["main"]["temp_min"]))
	print("| high temperature=", k2c(data["main"]["temp_max"]))
	print("| humidity=", data["main"]["humidity"])
	print("| pressure=", data["main"]["pressure"])
	print("| wind deg=", data["wind"]["deg"])
	print("| wind speed=", data["wind"]["speed"])
	print("")

