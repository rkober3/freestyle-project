# Freestyle Project: Residential Real Estate Investment Analysis Tool

## Requirements and Setup

From a mac on the terminal, navigate to the directory in which this repository has been cloned. To install the requirements, type 'pip3 install -r requirements.txt'. Then, add a file called '.env' to the repository and enter the text 'MY_API_KEY' = 'your_api_key' (you may need to visit <https://market.mashape.com/moneals/rent-estimate> to get your free api key). Save the file, as it will be necessary to request data from the server. Type 'python3 final-project.py' from the terminal to run the script.

## User Inputs

The user is asked to put in the street address, city, and state of the property they wish to analyze, the purchase price, percentage down, mortgage rate, mortgage term, and a number of different expenses. All user inputs are validated prior to making a request to the API, and loops until a valid input is given, rather than terminating the program.

## Program Outputs

The program prints a recommendation to buy the property or keep looking based on a first year cash on cash return (threshold set at 8%). Additionally, each time the program is run, a line is written to the 'properties.csv' file, capturing crucial information that the user may want to look back on or analyze further.
