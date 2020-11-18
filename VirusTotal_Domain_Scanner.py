import requests

key = "Enter your api key here"   # Add Your api Key

Search = input("Please Enter your Domain: ")
Search = Search.strip()

url = 'https://www.virustotal.com/vtapi/v2/domain/report?apikey='+key+'&domain='+Search

response = requests.get(url)
json_response = response.json()

print(json_response)
