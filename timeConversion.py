#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return a STRING.
# The function accepts STRING s as a parameter.


def timeConversion(s):
    # Extract hours, minutes, seconds, and day part from the input string
    hour = int(s[0:2])
    mint = int(s[3:5])
    sec = int(s[6:8])
    day = s[8:11]
    
    # Convert time to 24-hour format
    if hour < 12 and day == 'PM':
        hour += 12
    if hour == 12 and day == 'AM':
        hour -= 12
           
    # Format hours, minutes, and seconds as two-digit strings
    hour_str = '{:02d}'.format(hour)
    mint_str = '{:02d}'.format(mint)
    sec_str = '{:02d}'.format(sec)
    
    # Create the formatted time string
    time = hour_str + ':' + mint_str + ':' + sec_str 
    return time

# Read input in 12-hour format
s = input()

# Call the timeConversion function to convert and format the time
result = timeConversion(s)

# Print the result
print(result)
