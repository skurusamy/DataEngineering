import requests
import smtplib
from bs4 import BeautifulSoup
import datetime


now = datetime.datetime.now()



def extractWeb(url):
	phone_models = set()
	print("Extracting....")
	response = requests.get(url)
	soup = BeautifulSoup(response.text,'html.parser')
	#print(soup)
	for tag in soup.find_all():
		if tag.has_attr( "data-type" ) and tag["data-type"] == 'products' :
			phone_models.add(tag.text.strip())
	return phone_models
	





phone_models = extractWeb('https://www.apple.com/iphone/compare/')
content = '<HTML><Head></Head><body>'
content += 'phone_models'
content += '</body></html>'

print(phone_models)
