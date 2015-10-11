import requests
import json
import re
from app.apis.Google import GoogleApi

#------------------------HERE API--------------------------------------#
#get weather forecast and walking directions

class HereApi:
  def __init__(self):
    self.app_id = 'evk3TrU4UcresAseG8Da'
    self.app_code = 'z4yYohROherMZ57eHTsQUg'
    self.gapi = GoogleApi()

  def extract_data(self, forecast_for_day):
    # Input: forecast_for_day (dict)
    # Output: dict of desired values
    weekday = forecast_for_day['weekday']
    windspeed = forecast_for_day['windSpeed']
    winddirection = forecast_for_day['windDirection']
    precipitationprobability = forecast_for_day['precipitationProbability']
    hightemperature = forecast_for_day['highTemperature']
    return {
      "weekday": weekday,
      "windspeed": windspeed,
      "winddirection": winddirection,
      "precipitationprobability": precipitationprobability,
      "hightemperature": hightemperature
    }

  def get_weather(self, address):
    # Input: lat (float), lon (float)
    # Output: extracted data dicts (list)
    # {
    #   "country": "United States",
    #   "state": "California",
    #   "city": "Rochedale Village",
    #   "forecast": [
    #     {
    #       "hightemperature": "22.00",
    #       "windspeed": "18.87",
    #       "winddirection": "243",
    #       "weekday": "Saturday",
    #       "precipitationprobability": "10"
    #     },
    #     ...
    #   ]
    # }
    lat, lon = self.gapi.decode_address(address)
    resp = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?app_id=%s&app_code=%s&product=forecast_7days_simple&latitude=%s&longitude=%s' % (self.app_id, self.app_code, lat, lon))
    weather_data = json.loads(resp.content)
    forecasts = weather_data['dailyForecasts']['forecastLocation']['forecast']
    filtered_forecasts = [self.extract_data(fcst) for fcst in forecasts]
    result = {
      "forecast": filtered_forecasts,
      "country": weather_data['dailyForecasts']['forecastLocation']['country'],
      "state": weather_data['dailyForecasts']['forecastLocation']['state'],
      "city": weather_data['dailyForecasts']['forecastLocation']['city']
    }
    return json.dumps(result)

  def get_route(self, address0, address1):
    # Input: lat0, lon0, lat1, lon1 (floats)
    # Output: List of instructions for desired start and end location
    # {
    #   "directions": [
    #     "Head north on Prospect St. Go for 95 m.",
    #     "Turn left onto Bancroft Steps. Go for 191 m.",
    #     "Turn left onto Piedmont Ave. Go for 53 m.",
    #     "Turn right onto Durant Ave. Go for 214 m.",
    #     "Arrive at Durant Ave. Your destination is on the left."
    #   ],
    #   "summary": "The trip takes 553 m and 10 mins."
    # }
    lat0, lon0 = self.gapi.decode_address(address0)
    lat1, lon1 = self.gapi.decode_address(address1)
    url = 'http://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id=%s&app_code=%s&waypoint0=geo!%s,%s&waypoint1=geo!%s,%s&mode=fastest;pedestrian;traffic:disabled' % (self.app_id, self.app_code, lat0, lon0, lat1, lon1)
    resp = requests.get(url)
    resp = json.loads(resp.content)['response']['route'][0]
    summary = re.sub('<[^<]+?>', '', resp['summary']['text'])
    dirs = []
    for leg in resp['leg']:
      for manuever in leg['maneuver']:
        dirs.append(re.sub('<[^<]+?>', '', manuever['instruction']))
    result = {
      'summary': summary,
      'directions': dirs
    }
    return json.dumps(result)

if __name__ == '__main__':
  hapi = HereApi()
  address0 = '2327 warring st'
  print hapi.get_weather(address0)
  print hapi.get_route(address0, '2395 piedmont ave')
