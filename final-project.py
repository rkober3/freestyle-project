from   dotenv import load_dotenv
import requests
import urllib.parse
import json
import csv
import os

street_address = input("Please Enter a Street Address (No Abbreviations): ").title()
city = input("Please Enter a City in the United States: ").title()
state = input("Please Enter a State Abbeviation: ").upper()
address = str(street_address+", "+city+", "+state)
bedrooms = input("Please enter a number of bedrooms: ")
bathrooms = input("Please enter a number of bathrooms:")

load_dotenv()
api_key = os.environ.get("MY_API_KEY") or "OOPS. Please set an environment variable named 'MY_API_KEY'."
f = { 'address' : address, 'bathrooms' : bathrooms,'bedrooms':bedrooms}
url_code = urllib.parse.urlencode(f)

url = str("https://realtymole-rental-estimate-v1.p.mashape.com/rentalPrice?"+url_code)
headers = {
'X-Mashape-Key': api_key,
'Accept': 'text/plain'
}

response = requests.get(url, headers=headers)
all_data = json.loads(response.text)
print(response)
print(all_data)
rent_estimate = all_data['rent']
