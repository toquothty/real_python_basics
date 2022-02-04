# This space is just for chapter follow along and review exercises.
#


import mechanicalsoup
import time

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    time_rolled = page.soup.select("#time")[0]
    time_result = time_rolled.text
    print(f"the result of your dice roll is: {result} at {time_result}")
    if i < 3:
        time.sleep(4)
