import json
from StringIO import StringIO
import requests
import json
import pprint
import sys
#provide input parameter as user id e.g. 139010
try:
	usr_id_arg = str(sys.argv[1])
	saurl = 'http://api.stackexchange.com/2.2/users/'+str(usr_id_arg)+'/answers?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-&pagesize=100&page=1'
	#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
	#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
	print saurl
	resp = requests.get(saurl)
	resp.close()
	content	= resp.text
	fl = open("userAnswers.json", "w")
	fl.write(content)
	fl.close()
	
	contentJson = resp.json()
	pprint.pprint(contentJson)
 
	if resp.status_code == 200:
		#This means everything is ok
		#import pdb;pdb.set_trace()
		i=2
		if contentJson['has_more']:
			while i < 3:
				saurl = 'http://api.stackexchange.com/2.2/users/'+str(usr_id_arg)+'/answers?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-&pagesize=100&page='+str(i)
				#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
				#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
				resp = requests.get(saurl)
				content	= resp.text
				contentJson = resp.json()
				
				if contentJson['has_more']:
					i=i+1
					fl = open("userAnswers.json", "a+")
					fl.write('\n')
					fl.write(content)
					fl.close()
				else:
					break;
except Exception, e:
    print 'Something went wrong:', e