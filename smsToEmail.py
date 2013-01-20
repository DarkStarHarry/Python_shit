#http://null-byte.wonderhowto.com/how-to/send-sms-messages-with-python-0132938/
import urllib
import urllib2
def number2Email(number):
	#number = raw_input("Please Enter The Phone Number:\n")
	#message = raw_input("Please Enter Your Message:\n")
	prov = ''
	url2 = 'http://www.txt2day.com/lookup.php'
	url = 'http://www.onlinetextmessage.com/send.php'
	values2 = {'action' : 'lookup',
			   'pre' : number[0:3],
			   'ex' : number[3:6],
			   'myButton' : 'Find Provider'}
	data2 = urllib.urlencode(values2)  ##provider checker
	req2 = urllib2.Request(url2, data2)
	response2 = urllib2.urlopen(req2)
	the_page2 = response2.read()
	if 'Telus' in the_page2:
		prov = '@msg.telus.com'
	if 'Bell' in the_page2:
		prov = '@txt.bell.ca'
	if 'Rogers' in the_page2:
		prov = '@pcs.rogers.com'
	if 'Sprint' in the_page2:
		prov = '@messaging.sprintpcs.com'
	if 'T-Mobile' in the_page2:
		prov = '@tmomail.net'
	if 'Verizon' in the_page2:
		prov = '@vtext.com'
	if 'Virgin Mobile' in the_page2:
		prov = '@vmobl.com'
	if 'AT&T' in the_page2:
		prov = '@txt.att.net'
	if prov == 0:
		print "Failed To Identify Provider\n"
		return 0
	else:
		return number + prov
