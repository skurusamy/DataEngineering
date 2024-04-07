import requests
  
# Making a get request
response = requests.get('https://geeksforgeeks.org')
  
with open("sample.xml", "w") as fileobj:
    fileobj.write(response.text)
  