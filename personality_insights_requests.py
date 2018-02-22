import json
from os.path import join, dirname
import requests
from pymongo import MongoClient 

client = MongoClient()
db=client['semicolons']
jd = db.JobDescription

watson_url="https://gateway.watsonplatform.net/personality-insights/api/v3/profile?version=2017-10-13"
#    version='2017-10-13',
username='d1623e0d-a964-460b-a012-e0d596093ba4'
password='6pjhjO7h1ZNq'
jd_txt= open('salesforce.txt','r')
response = requests.post(watson_url,
                          auth=(username, password),
                          headers = {"content-type": "text/plain"},
			  params = {"raw_scores": True},
                          data=jd_txt.read()
                          )

insights= json.loads(response.text)
#with open('UI', 'w') as outfile:  
#    json.dump(insights, outfile,indent=2)

#insights = json.load(open('JD_1.json'))
#print json.dumps(response)
#print response
#print(json.dumps(insights))
for need in insights['needs']:
#    print need
    need['profile']="salesforce"
    jd.insert(need)
for person in insights['personality']:
#    print person
     person['profile']="salesforce"
     jd.insert(person)
for value in insights['values']:
    value['profile']="salesforce"
    jd.insert(value)

#print jd.count()
#needs = insights['needs']    
#jd.insert(needs) 
#jd.insert(insights['needs'])
