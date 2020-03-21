import urllib2

def main():
  url="https://google.com/"
  response = urllib2.urlopen(url)
  content = response.read()
  print(content)