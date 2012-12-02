# coding: utf-8
import httplib2
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer
http = httplib2.Http()
url = "http://www.mta.info/mnr/html/planning/schedules/schedules.htm"
status, response = http.request(url)
soup_object = BeautifulSoup(response)
Links = soup_object.findAll('a', {'href': re.compile('^pdf.*')})
for link in Links:
    print link
