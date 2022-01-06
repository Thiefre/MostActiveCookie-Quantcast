# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:19:01 2021

@author: Kevin Luu
"""

# Using Python shell, command is: python most_active_cookie.py FILENAME -d DATE
# If a DATE is NOT provided, it will display the most active cookie from the entire file; meaning date is disregarded
# If a DATE is provided, it will display the most active cookie from only that date

import argparse  
from datetime import datetime
        
def most_active_cookies(date, file_name):
            
    # Declare initial variables:
    maximum = 1 # keeps track of the highest amount of cookie occurences 
    table = {} # create a dictionary, or 'hashtable', to map cookies to # of occurences
    
    with open(file_name, 'r') as opened_file: 
        #Check if date is valid
        date_obj = date
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(date, ": Not a valid date or date is not provided, printing most active cookie disregarding date:")
            date = ""
        
        for line in opened_file:
            # Beginning of string parsing
            cookie, timestamp = line.split(",")
            timestamp = timestamp.strip()
            if "T" in timestamp:
                day, time = timestamp.split("T") # End of string parsing
                day = datetime.strptime(day, "%Y-%m-%d")
                # Checks if date of cookie equals the date we are checking, if no date provided in args check everything
                if day == date_obj or date == "":
                    # Creates or updates table entries, increment key/pair values by 1 if cookie is encountered again
                    value = table.get(cookie)
                    if value is None:
                        table[cookie] = 1
                    else:
                        table[cookie] += 1
                        # Maximum is updated to search for only most active cookies in the table later
                        if(table[cookie] > maximum):
                            maximum = table[cookie] # End of file parsing and table updating
                # If day is 'older' than date, break out since the log file is sorted by time
                elif(day < date_obj):
                    break
                        
    max_keys = [] # Array to hold all of the most active cookies
    # Searches through the hashtable for the most active cookies, checking if the # of occurrences == maximum
    for key in table:
        if table[key] == maximum:
            max_keys.append(key) # Adds that cookie to the resulting array
    
    # Walk through the array to print the most active cookies
    for key in max_keys:
        print(key)
        
    #Total run time = O(N+M+E)
    return max_keys

def parse_command_line_args():
    
    parser = argparse.ArgumentParser(description = 'Process date in UTC.')
    parser.add_argument('file', help = "file path of .csv for cookie_log", type = str)
    parser.add_argument('-d', nargs = "?", default = "", help = 'date in UTC', type = str)
    
    args = parser.parse_args()
    
    date = args.d # initial value of date variable, used to store the date from the CL arg
    file_name = args.file # cookie_logs file, with file name provided by CL arg
    
    return date, file_name

def main():
    date, file_name = parse_command_line_args()
    most_active_cookies(date, file_name)
    
if __name__ == '__main__':
    main()