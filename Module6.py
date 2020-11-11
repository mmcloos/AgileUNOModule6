"""
Maggie Cloos
Module 6
11/11/2020
cloosmm0@gmail.com
maggie.cloos@portnola.com
"""

import sys
import enum
import json

with open("input.json","r") as input:
    customers = json.load(input)

    
# are all customer numbers unique?
temp = []
for value in customers["clients"]:
    temp.append(value["id"])


# add values to set
unique = set(temp)
# add values to tuple
original = temp


if len(unique) != len(original):
    print("There are duplicate ID numbers in the data, exiting!!!")
    sys.exit()
else:
    print("All customer IDs are unique!")
        
"""
1.
create a set of customer emails & check for uniqueness
"""
temp = []
for value in customers["clients"]:
    temp.append(value["email"])

emails_unique = set(temp)
emails_original = temp

if len(emails_unique) != len(emails_original):
    print("There are duplicate emails! Exiting.")
    sys.exit()

else:
    print("All customer emails are unique.")


"""
2.
create a dictionary of each customer that contains name & email
write as a JSON file to a new file called email_list.json
"""

temp2 = {}
for value in customers["clients"]:
    temp2[value["name"]] = value["email"]

with open("email_list.json", "w") as outfile:
   json.dump(temp2, outfile) 


"""
3.
open the original file & set each male customer isActive to false
write the new data to a file called current_customers
"""

current_customers = customers
for clients in customers["clients"]:
    if clients["gender"] == "male":
       clients["isActive"] = False

with open("current_customers.json", "w") as outfile:
    json.dump(current_customers, outfile)



