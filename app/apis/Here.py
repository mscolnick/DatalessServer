import requests
import json
import re

#------------------------HERE API--------------------------------------#
#get weather forecast and walking directions

class HereApi:
  def __init__(self):
    self.app_id = 'evk3TrU4UcresAseG8Da'
    self.app_code = 'z4yYohROherMZ57eHTsQUg'

  def extract_data(self, forecast_for_day):
    # Input: forecast_for_day (dict)
    # Output: dict of desired values
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

  def get_weather(self, lat, lon):
    # Input: lat (float), lon (float)
    # Output: extracted data dicts (list)
    resp = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?app_id=%s&app_code=%s&product=forecast_7days_simple&latitude=%s&longitude=%s' % (self.app_id, self.app_code, lat, lon))
    weather_data = json.loads(resp.content)
    forecasts = weather_data['dailyForecasts']['forecastLocation']['forecast']
    return [self.extract_data(fcst) for fcst in forecasts]

  def get_route(self, lat0, lon0, lat1, lon1):
    # Input: lat0, lon0, lat1, lon1 (floats)
    # Output: List of instructions for desired start and end location
    url = 'http://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id=%s&app_code=%s&waypoint0=geo!%s,%s&waypoint1=geo!%s,%s&mode=fastest;pedestrian;traffic:disabled' % (self.app_id, self.app_code, lat0, lon0, lat1, lon1)
    resp = requests.get(url)
    resp = json.loads(resp.content)['response']['route'][0]
    legs = resp['leg']
    instrs = []
    for leg in legs:
      for manuever in leg['maneuver']:
        instrs += [re.sub('<[^<]+?>', '', manuever['instruction'])]
    return instrs

if __name__ == '__main__':
  hapi = HereApi()
  lat, lon = 37.868474037, -122.2503770
  print hapi.get_weather(lat,lon)
  print hapi.get_route(37.868474037,-122.2503770, 37.868336,-122.254682)
