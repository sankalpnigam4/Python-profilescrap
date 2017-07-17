import json
from StringIO import StringIO
import requests
import pprint

try:
	saurl = 'http://api.stackexchange.com/2.2/users?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page=1'
	#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
	#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
	resp = requests.get(saurl)
	
	content	= resp.text
	print str(content)
	content.replace("u'\uc6c3'",'\xec\x9b\x83')
	fl = open("manyUsers.json", "w")
	fl.write(str(content))
	fl.close()
	
	contentJson = resp.json()
 
	if resp.status_code == 200:
		#This means everything is ok
		#raise ApiError('GET /tasks/ {}'.format(resp.status_code))
		#print('resp')
		#print(resp.json())
		#print content
		#print content.find('"has_more":true')
		#import pdb;pdb.set_trace()
		i=2
		if contentJson['has_more']:
			#print("Found")
			while i < 3:
				saurl = 'http://api.stackexchange.com/2.2/users?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page='+str(i)
				#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
				#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
				print saurl
				resp = requests.get(saurl)
				content	= resp.text
				contentJson = resp.json()
				pprint.pprint(contentJson)
				if contentJson['has_more']:
					i=i+1
					fl = open("manyUsers.json", "a+")
					fl.write('\n')
					fl.write(content)
					fl.close()
				else:
					break;
except Exception, e:
    print 'Something went wrong:', e