# coding: utf-8
import httplib2, re
from BeautifulSoup import BeautifulSoup, SoupStrainer
http = httplib2.Http()
url = "http://www.mta.info/mnr/html/planning/schedules/schedules.htm"
status, response = http.request(url)
linkList = []
PDFLinks = []
for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_key('href'):
        linkList.append(link['href'])
for link in linkList:
	matchObj = re.match('pdf.*pdf', link)
    if matchObj:
	    PDFLinks.append(matchObj.group())

for link in PDFLinks:
	print link
