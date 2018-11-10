# Tool for automagically updating weakauras hosted on wago.io
# Currently WIP

# Import libs
import urllib2
from bs4 import BeautifulSoup

# URL
url = "http://wago.io/NyKyPWbZf"

# Header to avoid 403 error response
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.9',
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
       'Connection': 'keep-alive',
       'Accept-Encoding': 'none',
       'Accept-Langage': 'en-US,en;q=0.8'}

# Request with url and header
req = urllib2.Request(url, headers=hdr)

# Query the website
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

# Print page
print page.read()

# Parse
soup = BeautifulSoup(page, 'html.parser')

# Go through html soup to find import string
wago_string = soup.find(id="wago-importstring")

print wago_string
