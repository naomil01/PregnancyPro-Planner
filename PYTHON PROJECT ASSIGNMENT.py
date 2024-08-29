# Console App Name : PregnancyPro Planner 

# My Problem Scenario:
# I wanted to create a console application to assist couples in planning their pregnancy by using a Pregnancy Fertility Window API. 
# The application aims to interact with the Pregnancy Fertility Window API to retrieve fertility window data based on the user's menstrual cycle information. 
# It will then analyze this data to provide personalized recommendations for the best optimal conception timing , based on the user's menstrual cycle data. 

# I wanted to implement the following:
# User Input - to prompt the user to input their menstrual cycle data, including the start date of their last menstrual period (LMP) and the average length of their menstrual cycle.
# To use the Pregnancy Fertility Window API to fetch the fertility window data based on the user's input.
# Data Transformation - to analyze the fertility window data to calculate the most fertile days for conception. 

# The Pregnancy Calculator API,
# API offers a suite of powerful endpoints, providing users with accurate and reliable information for key milestones during pregnancy. 
# It provides the Fertility Window calculation pinpoints the most fertile days of a woman's menstrual cycle, aiding those trying to conceive and optimizing family planning decisions.

# TO ACCESS API-KEY 
# You have to create an account on the website , you will have to start a free trail subscription for 7 days to access an API-KEY.
# You will have to verify your account via email and put in your bank details but you will not be charged. You can delete the trail 
# after it is not longer required. 



import requests
import json

url = "https://zylalabs.com/api/2349/pregnancy+calculator+api/2267/fertility+window?cycle_length=28&menstrual_date=2023-06-01"
# Payload data item is stored a dictionary to POST and CREATE data.
payload = {
    'cycle_length': '28',
    'menstrual_date': '2023-06-01'
}
headers = {
    'Authorization': 'Bearer 3796|h2X9fJkJAahsWNMhjy3JV5JGqTqWTQZ4FNx8II73'}


# Using a GET request to get the API endpoint using requests library , this is stored as a string datatype.
response = requests.request("GET", url, headers=headers,data=payload)
# This is to print the API response without json
# print(response.text)

response_json =json.loads(response.text)
print(response_json)

# If I wanted to get the fertility_window_start date , I would use the dictionary method to print the value associated to this key.
# print(response_json['fertility_window_start'])
# The print would be 'Sat, 10 Jun 2023 00:00:00 GMT'


# Using a simple elif statement to check if the request was successful by looking at the status code
if response.status_code == 200:
    print("Success with request!")

elif response.status_code == 404:
    print('Request not found.')

else:
 print(f"Error:{response.status_code}")


# Parse the API response and storing the data in variables in json.  
# Using dictionary data type to store this data.
data = json.loads(response.text)
fertility_window_start = data["fertility_window_start"]
fertility_window_end = data["fertility_window_end"]


# Here I am defining the is_within_fertility_window function using string slicing as I want to focus on specfic parts of the start and end date of the fertility window. 
# to see if the date selected is within the window frame. 
# I am extracting the day, month, and year from the date strings.
# I am also using a boolean here as it takes a date as input and returns True if the date falls within the fertility window, and False if not.

def is_within_fertility_window(date):
    start_date = fertility_window_start[5:16]
    end_date = fertility_window_end[5:16]
    return start_date <= date <= end_date

# Testing the function with a date
date_to_check = "2023-06-21"
print(is_within_fertility_window(date_to_check))

# Adding a for loop to check multiple dates
# First , I am checking if a single date falls within the fertility window and then iterates through a list of dates, 
# printing whether each date falls within the window or not. 
# I have used a list beacuse it is easier to store multiple items in a single variable

dates_to_check = ["2023-06-21", "2023-06-16", "2023-06-17", "2023-06-24"]

print("Checking multiple dates within the fertility window:")
for date in dates_to_check:
    if is_within_fertility_window(date):
        print(f"{date} falls within the fertility window.")
    else:
        print(f"{date} does not fall within the fertility window.")


# This is the write to a file example 
with open('fertility_window_result.txt', 'w') as file:
        file.write("This is fertility window results \n" +
                   "fertility_window_end: Mon, 19 Jun 2023 00:00:00 GMT \n" +
                   "fertility_window_start: Sat, 10 Jun 2023 00:00:00 GMT \n" +
                   "Success with request! \n" + 
                   "False \n" +
                   "Checking multiple dates within the fertility window: \n" +
                   "2023-06-21 does not fall within the fertility window. \n" +
                   "2023-06-16 does not fall within the fertility window. \n" +
                   "2023-06-17 does not fall within the fertility window. \n" +
                   "2023-06-24 does not fall within the fertility window.")
        
        
