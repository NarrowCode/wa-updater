## Abandoned Project

This project was abandoned because an official version now exists! Repo kept for reference :)

# WA-Updater

An updating tool for weakauras from wago.io,
written in Python.

Generates a new textfile for each selected wago.io weakaura
with its current import string.

---

## Dependencies

**pip**

Using pip to install the rest of the dependencies

    easy_install pip

**BeautifulSoup**

Used to parse the website

    pip install BeautifulSoup4

**selenium**

Used for browser emulation with .js integration

    pip install selenium

**selenium webdriver for Firefox**

Tells selenium to use Firefox as a Browser

    curl -OL https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-macos.tar.gz 
    tar xvfz geckodriver-v0.23.0-macos.tar.gz
    mv geckodriver /usr/local/bin

In order for this to work, /usr/local/bin needs to be in the exectuion PATH
On mac, the folder can be added to /etc/paths to accomplish this

---

## Usage

Add the links to a wago.io page to the file wago-links.txt

The format must be

    link-to-wago.io,description

Call the scrapper using

    python scrapper.py
