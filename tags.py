import json
from StringIO import StringIO
import requests
import pprint

try:
	saurl = 'http://api.stackexchange.com/2.2/tags?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page=1'
	resp = requests.get(saurl)

	content	= resp.text
	fl = open("myTags.json", "w")
	fl.write(content)
	fl.close()
	
	contentJson = resp.json()
	#print contentJson.prettify()
	pprint.pprint(contentJson)
	if resp.status_code == 200:
		i=2
		if contentJson['has_more']:
			while i < 3:
				saurl = 'http://api.stackexchange.com/2.2/tags?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page='+str(i)
				resp = requests.get(saurl)
				content	= resp.text
				contentJson = resp.json()
				if contentJson['has_more']:
					i=i+1
					fl = open("myTags.json", "a+")
					fl.write('\n')
					fl.write(content)
					fl.close()
				else:
					break;
except Exception, e:
    print 'Something went wrong:', e
