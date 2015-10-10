import requests
import json
import re

#------------------------HERE API--------------------------------------#
#get weather forecast and walking directions

lat, lon = 37.868474037, -122.2503770
app_id = 'evk3TrU4UcresAseG8Da'
app_code = 'z4yYohROherMZ57eHTsQUg'

def extract_data(forecast_for_day):
  weekday = forecast_for_day['weekday']
  windspeed = forecast_for_day['windSpeed']
  winddirection = forecast_for_day['windDirection']
  precipitationprobability = forecast_for_day['precipitationProbability']
  hightemperature = forecast_for_day['highTemperature']
  return {"weekday": weekday,
      "windspeed": windspeed,
      "winddirection": winddirection,
      "precipitationprobability": precipitationprobability,
      "hightemperature": hightemperature}

def get_weather(lat, lon):
  resp = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?app_id=%s&app_code=%s&product=forecast_7days_simple&latitude=%s&longitude=%s' % (app_id, app_code, lat, lon))
  weather_data = json.loads(resp.content)
  forecasts = weather_data['dailyForecasts']['forecastLocation']['forecast']
  return [extract_data(fcst) for fcst in forecasts]

def get_route(lat0,lon0,lat1,lon1):
  url = 'http://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id=%s&app_code=%s&waypoint0=geo!%s,%s&waypoint1=geo!%s,%s&mode=fastest;pedestrian;traffic:disabled' % (app_id, app_code, lat0, lon0, lat1, lon1)
  resp = requests.get(url)
  resp = json.loads(resp.content)['response']['route'][0]
  legs = resp['leg']
  instrs = []
  for leg in legs:
    for manuever in leg['maneuver']:
      instrs += [re.sub('<[^<]+?>', '', manuever['instruction'])]
  return instrs

# resp = get_weather(lat,lon)
# print get_route(37.868474037,-122.2503770, 37.868336,-122.254682)
