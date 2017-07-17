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
count=0


#function to insert the record into the database

def insert(account_id,age,badge_counts,creation_date,display_name,is_employee,last_access_date,last_modified_date,link,location,profile_image,reputation,reputation_change_day,reputation_change_month,reputation_change_quarter,reputation_change_week,reputation_change_year,user_id,user_type,website_url):
         cursor.execute("insert into stackoverflow_users(account_id,age,badge_counts,creation_date,display_name,is_employee,last_access_date,last_modified_date,link,location,profile_image,reputation,reputation_change_day,reputation_change_month,reputation_change_quarter,reputation_change_week,reputation_change_year,user_id,user_type,website_url,tag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(account_id,age,badge_counts,creation_date,display_name,is_employee,last_access_date,last_modified_date,link,location,profile_image,reputation,reputation_change_day,reputation_change_month,reputation_change_quarter,reputation_change_week,reputation_change_year,user_id,user_type,website_url,tag_name))
         cnx.commit()
        
        
        




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

	if resp.status_code == 200:
                print "ram"
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
                users_list=[]
		for i in contentJson['items']:
			#print i['user']['user_id']
                        count+=1
			saurl = 'http://api.stackexchange.com/2.2/users/'+str(i['user']['user_id'])+'?site=stackoverflow&$$client_id=value$$&$$key=key_value$$((&Accept-Encoding=utf-8&pagesize=100&page=1'
			resp = requests.get(saurl)
			contentJsonUser = resp.json()
                        users_list.append(contentJsonUser)
                        #pprint.pprint(website_url)
                        #for j in contentJsonUser['items']:
                           # print j['display_name']
                           # print count
                            
	resp.close()
        
        for i in range(0,count):
                for j in users_list[i]['items']:
                        #pprint.pprint(j)
                        cursor.execute("select count(*) from stackoverflow_users where display_name = %s",(j['display_name'],))
                        result = cursor.fetchall()
                        for r in result:
                                chq=r[0]
                        if(chq==0):
                                 try:
                                          insert(j['account_id'],j['age'],j['badge_counts']['silver'],j['creation_date'],j['display_name'],j['is_employee'],j['last_access_date'],j['last_modified_date'],j['link'],j['location'],j['profile_image'],j['reputation'],j['reputation_change_day'],j['reputation_change_month'],j['reputation_change_quarter'],j['reputation_change_week'],j['reputation_change_year'],j['user_id'],j['user_type'],j['website_url'])
                                 except Exception, m:
                                     mystr= str(m)
                                     attr=mystr.replace("'","")
                                     if attr=='age':
                                              try:
                                                       insert(j['account_id'],' ',j['badge_counts']['silver'],j['creation_date'],j['display_name'],j['is_employee'],j['last_access_date'],j['last_modified_date'],j['link'],j['location'],j['profile_image'],j['reputation'],j['reputation_change_day'],j['reputation_change_month'],j['reputation_change_quarter'],j['reputation_change_week'],j['reputation_change_year'],j['user_id'],j['user_type'],j['website_url'])
                                              except Exception, l:
                                                       insert(j['account_id'],' ',j['badge_counts']['silver'],j['creation_date'],j['display_name'],j['is_employee'],j['last_access_date'],j['last_modified_date'],j['link'],' ',j['profile_image'],j['reputation'],j['reputation_change_day'],j['reputation_change_month'],j['reputation_change_quarter'],j['reputation_change_week'],j['reputation_change_year'],j['user_id'],j['user_type'],j['website_url'])
                                                       
                                         
                                     if attr=='location':
                                              insert(j['account_id'],j['age'],j['badge_counts']['silver'],j['creation_date'],j['display_name'],j['is_employee'],j['last_access_date'],j['last_modified_date'],j['link'],' ',j['profile_image'],j['reputation'],j['reputation_change_day'],j['reputation_change_month'],j['reputation_change_quarter'],j['reputation_change_week'],j['reputation_change_year'],j['user_id'],j['user_type'],j['website_url'])

                                              
except Exception, e:
    print 'Something went wrong:', e
    
