import urllib3
import json
import requests
import datetime


name = 'explorer'

for i in range(9):

	url = 'https://edassets.org/static/img/pilots-federation/'+name+'/rank-'+str(i+1)+'.png'
	r = requests.get(url)

	with open('img/ranks/'+name+'_rank'+str(i)+'.png', 'wb') as f:  
		f.write(r.content)

