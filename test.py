# This space is just for chapter follow along and review exercises.
#


from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# Exercise 1
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

# Exercise 2
print(profiles_page.soup.title.string)

# Exercise 3
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup


# Exercise 4
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDde"

profiles_page = browser.submit(form, login_page.url)
print(profiles_page.soup.center.text)
