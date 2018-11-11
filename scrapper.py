# Tool for automagically updating weakauras hosted on wago.io
# Currently WIP

# Import libs
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import csv
import shutil
import os

# Read input URLs from file
urls = []
desc = []

with open("wago-links.txt", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        urls.append(row[0])   
        desc.append(row[1])

# Browser configuration
opts = Options()
opts.set_headless()
assert opts.headless
browser = Firefox(options=opts)

count = 0

# Remove old output directory
shutil.rmtree("output")
os.mkdir("output")

for url in urls:
    browser.get(url)

    # Read into big soup
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # Go through html soup to find the import string
    wago_string = soup.find(id="wago-importstring").text.strip()

    print url
    
    out_file = open("output/" + desc[count] + ".txt", "w+")
    out_file.write(wago_string)
    count = count + 1
