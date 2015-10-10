## BingApi

#### bing_search
Outgoing 
```json
{"app_id": "0", "method": "bing_search", "params": ["dogs"]}
```
Incoming
```json
[
  {
    "Description": "Shane Barratt also agreed that more construction is needed rather than more speed cameras",
    "Title": "Readers have their say on A38 safety concerns | Burton Mail",
    "Url": "http://www.burtonmail.co.uk/Readers-say-A38-safety-concerns/story-27940928-detail/story.html"
  },
  ...
]
```

## CapitalOneApi

#### get_accounts
Outgoing 
```json
{"app_id": "1", "method": "get_accounts", "params": []}
```
Incoming
```json
[
  {
    "rewards": 11870,
    "customer_id": "560f0205f8d8770df0ef99da",
    "type": "Credit Card",
    "_id": "560f0207f8d8770df0efa460",
    "balance": 17181,
    "nickname": "Gerhardt's Account"
  },
  ...
]
```

#### get_account
Outgoing 
```json
{"app_id": "1", "method": "get_account", "params": ["560f0207f8d8770df0efa460"]}
```
Incoming
```json
{
  "rewards": 11870,
  "customer_id": "560f0205f8d8770df0ef99da",
  "type": "Credit Card",
  "_id": "560f0207f8d8770df0efa460",
  "balance": 17181,
  "nickname": "Gerhardts Account"
}
```

#### get_customers
Outgoing 
```json
{"app_id": "1", "method": "get_customers", "params": []}
```
Incoming
```json
[
  {
    "last_name": "OReilly",
    "first_name": "Skylar",
    "_id": "560f0205f8d8770df0ef99da",
    "address": {
      "city": "Swanton",
      "street_name": "Coopers Lane",
      "zip": "21561",
      "state": "Maryland",
      "street_number": "574"
    }
  },
  ...
]
```

## DataGovApi

#### get_ingredients
Outgoing 
```json
{"app_id": "2", "method": "get_ingredients", "params": ["bacon"]}
```
Incoming
```json
[
  {
    "group": "Proximates",
    "name": "Water",
    "nutrient_id": "255",
    "value": "0.25",
    "unit": "g"
  },
  ...
]
```

## HereApi

#### get_weather
Outgoing 
```json
{"app_id": "3", "method": "get_weather", "params": ["37.868474037", "-122.2503770"]}
```
Incoming
```json
{
  "country": "United States",
  "state": "California",
  "city": "Rochedale Village",
  "forecast": [
    {
      "hightemperature": "22.00",
      "windspeed": "18.87",
      "winddirection": "243",
      "weekday": "Saturday",
      "precipitationprobability": "10"
    },
    ...
  ]
}
```

#### get_route
Outgoing 
```json
{"app_id": "3", "method": "get_route", "params": ["37.868474037", "-122.2503770", "37.868336", "-122.254682"]}
```
Incoming
```json
{
  "directions": [
    "Head north on Prospect St. Go for 95 m.",
    "Turn left onto Bancroft Steps. Go for 191 m.",
    "Turn left onto Piedmont Ave. Go for 53 m.",
    "Turn right onto Durant Ave. Go for 214 m.",
    "Arrive at Durant Ave. Your destination is on the left."
  ],
  "summary": "The trip takes 553 m and 10 mins."
}
```
