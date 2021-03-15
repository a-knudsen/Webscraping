# Ahna Knudsen
# 3/14/2021
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

''' print statement returns: 
Profile: Dionysus





Name: Dionysus

Hometown: Mount Olympus

Favorite animal: Leopard

Favorite Color: Wine
'''

# find_all() to return a list of all instances of that tag
soup.find_all("img")
# make variables
image1, image2 = soup.find_all("img")
# Each Tag object has a .name property that returns a string containing the HTML tag type
image1.name
# returns 'img'
# You can access the HTML attributes of the Tag object by putting their name between square brackets
# Access the src attribute
image1["src"]
image2["src"]
# Certain tags in HTML documents can be accessed by properties of the Tag object.
# For example, to get the <title> tag in a document, you can use the .title property
soup.title
#  Retrieve the string between the title tags with the .string property of the Tag object
soup.title.string
# If you want to search for a specific image in the page:
soup.find_all("img", src="/static/dionysus.jpg")


