# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:28:32 2020

@author: DK
"""

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above 
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})
    





#🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

for item in travel_log:
    print(item)





