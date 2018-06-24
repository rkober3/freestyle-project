from   dotenv import load_dotenv
import requests
import urllib.parse
import json
import csv
import os

#Enter address for url input.
street_address = input("Please Enter a Street Address (No Abbreviations): ").title()
while True:
    if "Path" in street_address or "Street" in street_address or "Avenue" in street_address or "Road" in street_address or "Way" in street_address or "Drive" in street_address or "Court" in street_address or "Terrace" in street_address:
        break
    else:
        street_address = input("Please Enter a VALID Street Address (No Abbreviations): ").title()
city = input("Please Enter a City in the United States: ").title()
while True:
    if city in list:
        break
    else:
        city = input("Please Enter a VALID City in the United States: ").title()
state = input("Please Enter a State Abbeviation: ").upper()
while True:
    if state in list:
        break
    else:
        state = input("Please Enter a VALID State Abbreviation: ").upper()

#Concatonate address.
address = str(street_address+", "+city+", "+state)

#Enter number of beds and baths for url input.
bedrooms = input("Please enter a number of bedrooms: ")
while True:
    try:
        if type(int(bedrooms)) == int:
            break
    except ValueError:
        bedrooms = input("Please enter a VALID number of bedrooms (integers only): ")

bathrooms = input("Please enter a number of bathrooms:")
while True:
    try:
        if "." in bathrooms:
            if len(bathrooms.split(".", 1)[1]) <= 1:
                break
            else:
                bathrooms = input("Please enter a VALID number of bathrooms (max 1 number after decimal) :")
        elif type(int(bathrooms)) == int:
            break
        else:
            bathrooms = input("Please enter a VALID number of bathrooms (max 1 number after decimal) :")
    except ValueError:
        bathrooms = input("Please enter a VALID number of bathrooms (max 1 number after decimal) :")

#Enter mortgage inputs for calculation.
purchase_price = input("Please enter the purchase price of the property: ")
while True:
    try:
        if "." in purchase_price:
            if len(purchase_price.split(".", 1)[1]) <= 2:
                purchase_price = float(purchase_price)
                break
            else:
                purchase_price = input("Please enter a VALID purchase price (max 2 numbers after decimal) :")
        elif type(int(purchase_price)) == int:
            purchase_price = float(purchase_price)
            break
        else:
            purchase_price = input("Please enter a VALID purchase price (max 2 numbers after decimal) :")
    except ValueError:
        purchase_price = input("Please enter a VALID purchase price (max 2 numbers after decimal) :")

down = input("Please enter the percent of the purchase price to put down: ")
while True:
    try:
        if float(down) <= 1 and float(down) >= 0:
            down = float(down)
            break
        else:
            down = input("Please enter the percentage down as a decimal between 0 and 1: ")
    except ValueError:
        down = input("Please enter the percentage down as a decimal between 0 and 1: ")

rate = input("Please enter the mortgage rate: ")
while True:
    try:
        if float(rate) <= 1 and float(rate) >= 0:
            rate = float(rate)
            break
        else:
            rate = input("Please enter the mortgage rate as a decimal between 0 and 1: ")
    except ValueError:
        down = input("Please enter the mortgage rate as a decimal between 0 and 1: ")

term = input("Please enter the duration of the loan in years (integers only): ")
while True:
    try:
        if type(int(term)) == int:
            term = float(term)
            break
        else:
            term = input("Please enter a VALID duration for the mortgage in years (integers only): ")
    except ValueError:
        term = input("Please enter a VALID duration for the mortgage in years (integers only): ")

principal = purchase_price*(1-down)
interest = rate

#found on https://code.sololearn.com/c5kHd8o29UHG/#py
def monthly_loan(principal,interest_rate,duration):
    n = duration*12 #total number of months
    r = interest_rate/(100*12) #interest per month
    monthly_payment = principal*((r*((r+1)**n))/(((r+1)**n)-1)) #formula for compound interest applied on mothly payments.
    return monthly_payment
payment = monthly_loan(principal,interest,term)        
        
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
