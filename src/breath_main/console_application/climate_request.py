import requests, json, pdb, datetime

url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

city = input("Digite uma cidade omitindo os acentos e ç:")

pdb.set_trace()
querystring = {"q":city}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "24117470c7msh69c4f7f119cb290p144f8djsnfa7d413f68a3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

clima_data = None
if response.status_code == 200:
	clima_data = json.dumps(response.json(), indent = 4, sort_keys=False)

clima_data = True
if clima_data is not None:
	# Airmine AQI endpoint
	endpoint = "https://pm251.p.rapidapi.com/aqi"
	# Coordinates of Berlin
	coordinates = {
		"lat": clima_data['city']['coord']['lat'],
		"lon": clima_data['city']['coord']['lon']
	}
	# Custom headers
	headers = {
		'x-rapidapi-host': "pm251.p.rapidapi.com/aqi",
		'x-rapidapi-key': "24117470c7msh69c4f7f119cb290p144f8djsnfa7d413f68a3"
	}

	# Execute a GET request
	response = requests.request(
		  "GET", endpoint,
		  headers = headers, params = coordinates
	)

	air_data = None
	if response.status_code == 200:
		air_data = response.json()

	if air_data is not None:
		n = len(air_data['forecasts'])	
		for item in air_data['forecasts']:
			date = item['date']
			d1 = datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M:%S")
			d2 = datetime.datetime.now()
			pm25 = item['values'][0]['value']
			if (d1 > d2):
				print("%s | %d pm25" % (date, pm25))
				break
			else:
				print(date, 'futuro')	
		#remaining = int(response.headers['x-ratelimit-requests-remaining'])
 		#print("You have %d requests left" % remaining)
else:
	print("Nao possuimos informacoes da sua cidade")
