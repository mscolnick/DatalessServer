import requests # Get from https://github.com/kennethreitz/requests
import string

# static Wrapper for Bing Search API (do not use though)
class BingSearchAPI():
    bing_api = "https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Composite?"

    def __init__(self, key):
        self.key = key

    def replace_symbols(self, request):
        # Custom urlencoder.
        # They specifically want %27 as the quotation which is a single quote '
        # We're going to map both ' and " to %27 to make it more python-esque
        request = string.replace(request, "'", '%27')
        request = string.replace(request, '"', '%27')
        request = string.replace(request, '+', '%2b')
        request = string.replace(request, ' ', '%20')
        request = string.replace(request, ':', '%3a')
        return request

    def search(self, sources, query, params):
        ''' This function expects a dictionary of query parameters and values.
            Sources and Query are mandatory fields.
            Sources is required to be the first parameter.
            Both Sources and Query requires single quotes surrounding it.
            All parameters are case sensitive. Go figure.
            For the Bing Search API schema, go to http://www.bing.com/developers/
            Click on Bing Search API. Then download the Bing API Schema Guide
            (which is oddly a word document file...pretty lame for a web api doc)
        '''
        request =  'Sources="' + sources    + '"'
        request += '&Query="'  + str(query) + '"'
        for key,value in params.iteritems():
            request += '&' + key + '=' + str(value)
        request = self.bing_api + self.replace_symbols(request)
        return requests.get(request, auth=(self.key, self.key))


#------------------------Bing Search------------------------------------#

class BingApi:
  def __init__(self):
    my_key = "abwz7dDyF/DoVzamPRewH0Awh/rJCL8AkDyAfFr4Cbs"
    self.bing = BingSearchAPI(my_key)

  def search(self, query, num_results):
    # Input: query (string), num_results (int)
    # Output: num_results results of query
    params = {'$format': 'json',
            '$top': num_results,
            '$skip': 0}

  def bing_search(self, query):
    # Input: query (string)
    # Output: list of results, descriptions and urls
    params = {'$format': 'json',
                '$top': 10,
                '$skip': 0}
    a = self.bing.search('web',query,params).json()
    results_list = a['d']['results'][0]['Web']
    results = []
    descriptions = []
    urls = []
    for result in results_list:
      results += [result['Title']]
      descriptions += [result['Description']]
      urls += [result['Url']]
    return results, descriptions, urls

if __name__ == '__main__':
  bapi = BingApi()
  results, descriptions, urls = bapi.bing_search("shane barratt")
  for i in range(len(results)):
    print results[i]
    print descriptions[i]
    print urls[i]
    print "-"
