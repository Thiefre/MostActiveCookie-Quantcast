# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:19:01 2021

@author: Kevin Luu
"""

# Using Python shell, command is: python most_active_cookie.py FILENAME -d DATE

import sys

def most_active_cookies(date, file):
    
    # Declare initial variables:
    maximum = 1 # keeps track of the highest amount of cookie occurences 
    table = {} # create a dictionary, or 'hashtable', to map cookies to # of occurences
    
    try:
        # Reads each line from the file one by one, parses the information, and updates it into the hashtable
        for line in file:
            # Beginning of string parsing
            cookie, timestamp = line.split(",")
            timestamp = timestamp.strip()
            if("T" in timestamp):
                day, time = timestamp.split("T") # End of string parsing
                
                # Checks if date of cookie equals the date we are checking, if no date provided in args check everything
                if(day == date or date == ""):
                    # Creates or updates table entries, increment key/pair values by 1 if cookie is encountered again
                    value = table.get(cookie)
                    if(value == None):
                        table[cookie] = 1
                    else:
                        table[cookie] += 1
                        # Maximum is updated to search for only most active cookies in the table later
                        if(table[cookie] > maximum):
                            maximum = table[cookie] # End of file parsing and table updating
                # If day is 'older' than date, break out since the log file is sorted by time
                elif(day < date):
                    break
    except ValueError:
        print("Not a valid file!")
                        
    max_keys = [] # Array to hold all of the most active cookies
    # Searches through the hashtable for the most active cookies, checking if the # of occurrences == maximum
    for key in table:
        if(table[key] == maximum):
            max_keys.append(key) # Adds that cookie to the resulting array
    
    # Walk through the array to print the most active cookies
    for key in max_keys:
        print(key)
    #Total run time = O(N+M+E)
    
    return max_keys

def parse_command_line_args():
    date = "" # initial value of date variable, used to store the date from the CL arg
    file = open(sys.argv[1]) # open cookie_logs file, with file name provided by CL arg
    # Checks if date arguments are given
    if(len(sys.argv) > 2):
        date = sys.argv[3]
    return date, file

def main():
    date, file = parse_command_line_args()
    most_active_cookies(date, file)
    file.close()
    
if __name__ == '__main__':
    main()