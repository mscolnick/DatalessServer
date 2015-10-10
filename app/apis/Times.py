import requests
import json
import IPython as ipy

# http://developer.nytimes.com/docs/
class TimesApi:
  def __init__(self):
    self.article_search_key = '751708584532f20e3931b344b60bcd96:11:73183577'
    self.topstories_key = '64ed8cf95f90a456d86d42c819ea7863:16:73183577'

  def get_articles(self, search_query):
    # Input: search_query (string) - what you want to search for
    # Output: list of string json objects which contain headline, abstract and web_url
    uri = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&sort=newest&api-key=%s' % (search_query, self.article_search_key)
    resp = json.loads(requests.get(uri).content)
    resp = resp["response"]["docs"]

    filtered = []
    for result in resp:
      filtered += [{
        'headline': result['headline']['main'],
        'abstract': result['lead_paragraph'],
        'web_url': result['web_url']
      }]
    return json.dumps(filtered) 

  def get_topstories(self, section='world'):
    # Input: section = home, world, national, politics, nyregion, business, opinion, technology, science, health, sports, arts, fashion, dining, travel, magazine, realestate
    # Output: list of string json objects which contain headlines, abstracts and web_urls for top stories
    section = section.lower()
    assert section in ["home", "world", "national", "politics", "nyregion", "business", "opinion", "technology", "science", "health", "sports", "arts", "fashion", "dining", "travel", "magazine", "realestate"], "Invalid section"
    uri = 'http://api.nytimes.com/svc/topstories/v1/%s.json?api-key=%s' % (section, self.topstories_key)
    resp = json.loads(requests.get(uri).content)
    resp["results"]

    filtered = []
    for result in res:
      filtered += [{
        'headline': result['title'],
        'abstract': result['abstract'],
        'web_url': result['url']
      }]
    return json.dumps(filtered)

if __name__ == '__main__':
  times_api = TimesApi()
  # print times_api.get_news(37.7777,-120.2323)
  print times_api.get_articles('New York')
  print times_api.get_topstories('world')
