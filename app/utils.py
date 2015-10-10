import re
def cleanString(string):
  ascii_string = string.decode('unicode_escape').encode('ascii', 'ignore')
  return re.sub('\\\u....','',ascii_string)

