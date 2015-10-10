
def cleanString(string):
  return string.decode('unicode_escape').encode('ascii', 'ignore')

def fix_number(number, size):
  return str(number)[:size].zfill(size)
