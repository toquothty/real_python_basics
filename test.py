# This space is just for chapter follow along and review exercises.
#

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

url_list = []

for link in soup.find_all("a"):
    url_list.append(link["href"])

for profile in url_list:
    new_url = "http://olympus.realpython.org" + profile
    print(new_url)
    page = urlopen(new_url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text())
