import json
from StringIO import StringIO
import requests
import sys
#program needs a input as user id which is a numeric value
try:
	user_id = str(sys.argv[1])
	#example user id 2988

	#http://api.stackexchange.com/2.2/users/2988/tags?order=desc&sort=popular&site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-&pagesize=100&page=1
	saurl = 'http://api.stackexchange.com/2.2/users/'+str(user_id)+'/tags?order=desc&sort=popular&site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-&pagesize=100&page=1'
	#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
	#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
	resp = requests.get(saurl)

	content	= resp.text
	fl = open("topUsersByTagsAndTheirContri"+user_id+"_1.json", "w")
	fl.write(content)
	fl.close()

	contentJson = resp.json()

	if resp.status_code == 200:
		#This means everything is ok
		#raise ApiError('GET /tasks/ {}'.format(resp.status_code))

		#import pdb;pdb.set_trace()
		#i=2

		if contentJson['has_more']:

			result_has_more = str(contentJson['has_more'])

			
			i = 2

			while result_has_more == 'True':

				saurl = 'http://api.stackexchange.com/2.2/users/'+str(user_id)+'/tags?order=desc&sort=popular&site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-&pagesize=100&page='+str(i)
				#replace $$client_id=value with client_id=12345 (the value of client id that you will receive after you register your app)
				#replace $$key=key_value$$ with key=your key value (the key value that you will receive after you register your app)
				resp = requests.get(saurl)
				content	= resp.text
				contentJson = resp.json()

				fl = open("topUsersByTagsAndTheirContri"+user_id+"_"+str(i)+".json", "w")

				fl.write(content)
				fl.close()
				result_has_more = str(contentJson['has_more'])
				i=i+1
except Exception, e:
    print 'Something went wrong:', e