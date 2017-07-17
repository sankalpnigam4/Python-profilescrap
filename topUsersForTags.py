import json
from StringIO import StringIO
import requests
import pprint
import sys
import mysql.connector
import MySQLdb

#database connection

cnx = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="considerproject")

cursor = cnx.cursor()

try:
	tag_name = str(sys.argv[1])
	saurl = 'http://api.stackexchange.com/2.2/tags/'+str(tag_name)+'/top-answerers/all_time?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page=1'
	resp = requests.get(saurl)

	content	= resp.text
	#content=PrettyPrinter.pformat(resp)
	fl = open("topUsers"+str(tag_name)+".json", "w")
	fl.write(content)
	fl.close()
	
	contentJson = resp.json()
	#PrettyPrinter.pformat(contentJson)
	#pprint.pprint(contentJson)
	#print contentJson
        users_list=[]
	if resp.status_code == 200:
		i=2
		if contentJson['has_more']:
			while i < 3:
				saurl = 'http://api.stackexchange.com/2.2/tags/'+str(tag_name)+'/top-answerers/all_time?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page='+str(i)
				resp = requests.get(saurl)
				content	= resp.text
				contentJson = resp.json()
				if contentJson['has_more']:
					i=i+1
					fl = open("topUsers"+str(tag_name)+".json", "a+")
					fl.write('\n')
					fl.write(content)
					fl.close()
				else:
					break;
                
		for i in contentJson['items']:
			#print i['user']['user_id']
			saurl = 'http://api.stackexchange.com/2.2/users/'+str(i['user']['user_id'])+'?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page=1'
			resp = requests.get(saurl)
			contentJsonUser = resp.json()
                        users_list.append(contentJsonUser)
                       # pprint.pprint(website_url)
		       #for j in contentJsonUser['items']:
                           #print j['display_name']
	resp.close()
        for j in users_list[0]['items']:
                pprint.pprint(j['display_name'])

        pprint.pprint(users_list[0]['items'][0]['display_name'])
                
        
except Exception, e:
    print 'Something went wrong:', e
