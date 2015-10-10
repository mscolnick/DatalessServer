### Quick Start

Clone the repo, then:

```sh
$ git remote rm origin
$ git remote add origin <the location of my new git repository>
$ git push -u origin master
```

## Run

```sh
$ make server
```

## App ID Mapper

```json
mapper = {
  "0": BingApi,
  "1": CapitalOneApi,
  "2": DataGovApi,
  "3": HereApi,
  "4": SigimeraApi
}
```

## API examples
```json
{"app_id": "0", "method": "bing_search", "params": ["dogs"]}


{"app_id": "1", "method": "get_accounts", "params": []}
{"app_id": "1", "method": "get_account", "params": ["560f0207f8d8770df0efa460"]}
{"app_id": "1", "method": "get_customers", "params": []}


{"app_id": "2", "method": "get_ingredients", "params": ["bacon"]}


{"app_id": "3", "method": "get_weather", "params": ["37.868474037", "-122.2503770"]}
{"app_id": "3", "method": "get_route", "params": ["37.868474037", "-122.2503770", "37.868336", "-122.254682"]}
```
