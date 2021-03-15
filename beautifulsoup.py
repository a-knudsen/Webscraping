# Working with Beauitful Soup library, an HTML parser. 
# in command prompt install Beautiful Soup
pip install beautifulsoup4
pip show beautifulsoup4

# in editor, create a Beautiful Soup object
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
# Open the URL
page = urlopen(url)
# Read the HTML from the page as a string and assign it to the html variable
html = page.read().decode("utf-8")
# Create a BeautifulSoup object and assigns it to the soup variable
# The first argument is the HTML to be parsed and the second argument is the built-in HTMl parser 
soup = BeautifulSoup(html, "html.parser")
# 
print(soup.get_text())


Profile: Dionysus





Name: Dionysus

Hometown: Mount Olympus

Favorite animal: Leopard

Favorite Color: Wine



