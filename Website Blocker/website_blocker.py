# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:05:15 2018

@author: Vidhisha
"""

from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect= "12.0.0.1"
website_list=["www.hulu.com","hulu.com"]

while True:
    if dt(dt.now().year, dt.now().month , dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month , dt.now().day,16):
        print('Working Hours')
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+website)
    else:
        print('Fun Hours')
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
