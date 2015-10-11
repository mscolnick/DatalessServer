import re
def cleanString(string):
  ascii_string = string.decode('unicode_escape').encode('ascii', 'ignore')
  ascii_string = ascii_string.replace('"', "\"")
  return re.sub('\\\u....','',ascii_string)

def fix_number(number, size):
  return str(number)[:size].zfill(size)
