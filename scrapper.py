# Tool for automagically updating weakauras hosted on wago.io
# Currently WIP

# Import libs
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# Read input URLs from file
urls = []
file = open("wago-links.txt", "r")
for line in file:
   urls.append(line) 

# Browser configuration
opts = Options()
opts.set_headless()
assert opts.headless
browser = Firefox(options=opts)

for url in urls:
    browser.get(url)

    # Read into big soup
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # Go through html soup to find the import string
    wago_string = soup.find(id="wago-importstring").text.strip()

    print wago_string
