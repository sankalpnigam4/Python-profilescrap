import json
from StringIO import StringIO
import requests
import json
import sys
#provide input parameter as which is id of an answer e.g. 22534977
try:
	ans_id_arg = str(sys.argv[1])
	saurl = 'http://api.stackexchange.com/2.2/answers/'+str(ans_id_arg)+'?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-&pagesize=100&page=1'
	#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
	#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
	print saurl
	resp = requests.get(saurl)
	resp.close()
	content	= resp.text
	print content
	
	fl = open("userAnswersRating.json", "w")
	fl.write(content)
	fl.close()
	
	contentJson = resp.json()
	#import pdb;pdb.set_trace()
	print str(contentJson['items'][0]['score'])
	print('-----')
	print('-----')
except Exception, e:
    print 'Something went wrong:', e