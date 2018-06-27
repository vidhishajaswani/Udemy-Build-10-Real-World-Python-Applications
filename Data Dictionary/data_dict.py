# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 00:59:09 2018

@author: Vidhisha
"""

import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def val_of_key(key):
    key=key.lower()
    if key in data:
        return data[key]
    elif key.title() in data.keys():
        return data[key.title()]  
    elif key.upper() in data.keys():
        return data[key.upper()]  
    elif len(get_close_matches(key,data.keys()))>0:
        print("Did you mean %s instead? " %get_close_matches(key,data.keys())[0])
        print("Select Y for Yes, or N for No")
        yes_no=input()
        if yes_no=='Y' or yes_no=='y':
            return data[get_close_matches(key,data.keys())[0]]
        else:
            return 'Sorry, This word does not exist. Please double check it.'
    else:
        return 'Sorry, This word does not exist. Please double check it.'
    


word=input("Enter word: ")
output=val_of_key(word)

if type(output)==list:
            for value in output:
                print(value)
else:
   print(output)