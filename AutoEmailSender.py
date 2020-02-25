import feedparser
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib


data = feedparser.parse('http://feeds.feedburner.com/AlizaibHassan') #your feedburner url

#fetching the title of post
postTitle = data.entries[0].title

#fetching the link of post
postLink = data.entries[0].links[1].href
postLink = postLink.replace('#comment-form', '')

# fetching the summary from blog
soup = BeautifulSoup(data.entries[0].summary,"html.parser")
summary = soup.get_text()

#Sendind Email ...
gmail_user = 'yourmail@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to = ['receive1@gmail.com', 'receive2@gmail.com']
subject = 'Latest Blog Post '+postTitle
body = 'Title of Article: '+postTitle+'\n\n'+'Article URL: '+postLink+'\n\n'+'Summray: '+summary+'\n'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except:
    print('Something went wrong...')