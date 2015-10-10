
def cleanString(string):
  return string.decode('unicode_escape').encode('ascii', 'ignore')

