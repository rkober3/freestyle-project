from   dotenv import load_dotenv
import requests
import urllib.parse
import json
import csv
import os

def read_contents_from_file(filename="us_cities_states_counties.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    list = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            list.append(row)
    return list
list = str(read_contents_from_file())

def read_properties_from_file(filename="properties.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    properties = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            #print("#",row["id"],":",row["name"])
            properties.append(row)
    return properties
properties = read_properties_from_file()

def write_properties_to_file(filename="properties.csv", properties = properties):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)

    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["street_address","city","state","purchase_price","down","interest","rent_estimate","total_expenses","monthly_net_income","first_year_cash_on_cash"])
        writer.writeheader() # uses fieldnames set above
        for p  in properties:
            writer.writerow(p)
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

taxes = input("Please enter estimated annual real estate taxes: ")
while True:
    try:
        if "." in taxes:
            if len(taxes.split(".", 1)[1]) <= 2:
                taxes = float(taxes)/12
                break
            else:
                taxes = input("Please enter a VALID annual real estate tax estimate (max 2 numbers after decimal): ")
        elif type(int(taxes)) == int:
            taxes = float(taxes)/12
            break
        else:
            taxes = input("Please enter a VALID annual real estate tax estimate (max 2 numbers after decimal): ")
    except ValueError:
        taxes = input("Please enter a VALID annual real estate tax estimate (max 2 numbers after decimal): ")

utilities = input("Please enter estimated monthly utility expense: ")
while True:
    try:
        if "." in utilities:
            if len(utilities.split(".", 1)[1]) <= 2:
                utilities = float(utilities)
                break
            else:
                utilities = input("Please enter a VALID utilities expense estimate (max 2 numbers after decimal): ")
        elif type(int(utilities)) == int:
            utilities = float(utilities)
            break
        else:
            utilities = input("Please enter a VALID utilities expense estimate (max 2 numbers after decimal): ")
    except ValueError:
        utilities = input("Please enter a VALID utilities expense estimate (max 2 numbers after decimal): ")

management_fees = input("Please enter estimated monthly management fees: ")
while True:
    try:
        if "." in management_fees:
            if len(management_fees.split(".", 1)[1]) <= 2:
                management_fees = float(management_fees)
                break
            else:
                management_fees = input("Please enter a VALID estimate for management fees (max 2 numbers after decimal) :")
        elif type(int(management_fees)) == int:
            management_fees = float(management_fees)
            break
        else:
            management_fees = input("Please enter a VALID estimate for management fees (max 2 numbers after decimal) :")
    except ValueError:
        management_fees = input("Please enter a VALID estimate for management fees (max 2 numbers after decimal) :")

hoa = input("Please enter monthly HOA fees (if not applicable, enter '0'): ")
while True:
    try:
        if "." in hoa:
            if len(hoa.split(".", 1)[1]) <= 2:
                hoa = float(hoa)
                break
            else:
                hoa = input("Please enter a VALID HOA fee (max 2 numbers after decimal) :")
        elif type(int(hoa)) == int:
            hoa = float(hoa)
            break
        else:
            hoa = input("Please enter a VALID HOA fee (max 2 numbers after decimal) :")
    except ValueError:
        hoa = input("Please enter a VALID HOA fee (max 2 numbers after decimal) :")

expenses = [utilities,taxes,management_fees,hoa]

total_expenses = sum(expenses)
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
#print(response)
#print(all_data)
rent_estimate = all_data['rent']

passthrough_tax_rate = 0.20

monthly_net_income = (rent_estimate - payment - total_expenses)*(1-passthrough_tax_rate)
first_year_cash_on_cash = (monthly_net_income*12)/(purchase_price*down)

#Formatting variables for printing and writing to csv file.
first_year_percent = "{0:.2f}%".format(first_year_cash_on_cash*100)
purchase_price = "${0:,.2f}".format(purchase_price)
monthly_net_income = "${0:,.2f}".format(monthly_net_income)
interest = "{0:.2f}%".format(interest*100)
down = "{0:.2f}%".format(down*100)
rent_estimate = "${0:,.2f}".format(rent_estimate)
total_expenses = "${0:,.2f}".format(total_expenses)

#Printing outputs.
if first_year_cash_on_cash >= .08:
    print("You found a great property, earning "+first_year_percent+" in the first year!")
    print("Address: "+address)
    print("Purchase Price: "+purchase_price)
    print("Monthly Rental Revenue: "+rent_estimate)
    print("Monthly Net Income: "+monthly_net_income)
else:
    print("The property you input might not be the best. It only earns "+first_year_percent+" in the first year.")
    print("Keep Looking!")
    print("Address: "+address)
    print("Purchase Price: "+purchase_price)
    print("Monthly Rental Revenue: "+rent_estimate)
    print("Monthly Net Income: "+monthly_net_income)

new_property ={"street_address":street_address,"city":city,"state":state,"purchase_price":purchase_price,"down":down,"interest":interest,"rent_estimate":rent_estimate,"total_expenses":total_expenses,"monthly_net_income":monthly_net_income,"first_year_cash_on_cash":first_year_percent}
properties = properties.append(new_property)

write_properties_to_file()
