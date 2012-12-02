# coding: utf-8
import BeautifulSoup
import urllib2
import smtplib
url = 'http://www.mta.info/mnr/html/planning/schedules/schedules.htm'
fd = urllib2.urlopen(url)
soup = BeautifulSoup.BeautifulSoup(fd)
myLinks = soup.find('a href=')
print len(myLinks)
myLinks = soup.findAll('a')
print len(myLinks)
get_ipython().show_usage()
get_ipython().magic(u"logstart 'c:\\\\myHistory.py'")
get_ipython().magic(u'help')
get_ipython().magic(u'?')
get_ipython().magic(u'%help')
get_ipython().magic(u'%save')
get_ipython().magic(u'save')
get_ipython().magic(u"save 'c:\\myscript.py'")
get_ipython().magic(u"save 'myscript.py'")
get_ipython().magic(u'pinfo %save')
get_ipython().magic(u'save MNRRScrape')
get_ipython().magic(u'save filename MNRRScrape')
get_ipython().magic(u'save filename MNRRScrape.py')
get_ipython().magic(u"save filename 'MNRRScrape.py'")
get_ipython().magic(u'save MNRRScrape.py')
get_ipython().magic(u'save MNRRScrape')
get_ipython().magic(u"save 'MNRRScrape'")
get_ipython().magic(u'save MNRRScrape 1:25')
get_ipython().magic(u'save MNRRScrape 1:10')
print myLinks[1]
print myLinks[1].address
print myLinks[1].href
print myLinks[1].url
dir(myLinks[1])
print myLinks[1].index
print myLinks[1].string
print myLinks[1].extract
print myLinks[25]
print myLinks[24]
print myLinks[23]
print myLinks[22]
print myLinks[21]
print myLinks[20]
print myLinks[5]
print myLinks[6]
print myLinks[10]
print myLinks[15]
print myLinks[20]
print myLinks[18]
print myLinks[15]
print myLinks[12]
print myLinks[30]
print myLinks[29]
print myLinks[29].href
print myLinks[29].address
get_ipython().magic(u'save MNRRScrape 1:')
get_ipython().magic(u'save MNRRScrape')
get_ipython().magic(u'save MNRRScrape')
get_ipython().magic(u'save MNRRScrape :')
get_ipython().magic(u'save MNRRScrape 1:100')
get_ipython().magic(u'save MNRRScrape all')
get_ipython().magic(u'save MNRRScrape -all')
get_ipython().magic(u'save MNRRScrape []')
get_ipython().magic(u'save MNRRScrape 1:1000')