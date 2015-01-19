import re
import sys
import urlparse
import urllib
from bs4 import BeautifulSoup
class MyOpener(urllib.FancyURLopener):
    version ='Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

def convertURLtoPlaylist(url,filePath):
	myopener = MyOpener()
	#url = 'http://www.panicstream.com/streams/wsp/2012_12_30/'
	page = myopener.open(url)
	text = page.read()
	page.close()
	soup = BeautifulSoup(text)
	t = []
	m3uLines = []
	m3uLines.append('#EXTM3U')
	lineTemplate = "#EXTINF:-1, Widespread Panic - title"
	for tag in soup.findAll('a',href=True):
		tag['href'] = urlparse.urljoin(url, tag['href'])
		#print tag['href']
		theTag = tag['href']
		t.append(theTag)
		if theTag.find("mp3") == -1:
			t.pop()
		else:
			theFile = theTag.replace(url,"")
			theFile = theFile.replace("%20"," ")
			myLine = lineTemplate.replace('title',theFile)
			m3uLines.append(myLine)
			m3uLines.append(theTag)
	f = open(filePath, 'w')

	for i in m3uLines:
		#print i + '\n'
		f.write(i + '\n')
	f.close()
if __name__ == "__main__":
	convertURLtoPlaylist(sys.argv[1],sys.argv[2])