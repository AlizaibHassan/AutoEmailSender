import feedparser
from bs4 import BeautifulSoup
from datetime import datetime


data = feedparser.parse('http://feeds.feedburner.com/AlizaibHassan')
totalPosts = len(data.entries)


	#fetching the title of post
print(data.entries[0].title)

	#fetching the link of post
print(data.entries[0].link)

	# fetching the summary from blog
soup = BeautifulSoup(data.entries[0].summary,"html.parser")
summary = soup.get_text()
print(summary)

	#fetching the article published date
print(data.entries[0].published_parsed)

	#fetching current date and time
now = datetime.now()
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

