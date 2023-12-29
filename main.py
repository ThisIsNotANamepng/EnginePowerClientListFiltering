"""
This file takes a .txt file formatted as 

CLIENT NUMBER    CLIENT NAME (MIGHT HAVE SPACES, ALL CAPS)          CLIENT ADDRESS                         CREDIT LIMIT
         SECOND ADDRESS
         CITY         STATE CODE ZIP CODE           PHONE NUMBER
01010    CLIENT NAME EXAMPLE     623 STATE AVE                        50
 
         CITYVILLE            AA 03232           999/867-5309

And returns a csv file formatted as 

client number, client name, client address, client credit limit, second address, city, state code, zip code, phone number
01010, CLIENT NAME EXAMPLE, 623 STATE AVE, 50, UNKNOWN, CITYVILLE, AA, 03232, 9998675309

There might not be a credit limit or a second address

"""

import re

filename="CT"

def save(clientNumber, clientName, clientAddress, secondAddress, city, stateCode, zipCode, phoneNumber, creditLimit, filename):
    # Function to save all data sifted into filename.csv

    f=open(filename+".csv", "a")
    f.write('"'+clientNumber+'","'+clientName+'","'+clientAddress+'","'+secondAddress+'","'+city+'","'+stateCode+'","'+zipCode+'","'+phoneNumber+'","'+creditLimit+'"\n')
    f.close()

f = open(filename+".csv", "w") 
f.close()
# Creates the file to write to later, if it exists it gets overwitten as empty

f = open(filename+".TXT", "r")
lines = f.readlines()
lineIndex=0

for line in lines:
    lineIndex+=1

    splits=(re.split(r'\s{2,}', line))
    splits=list(filter(lambda x: x != '', splits))


    if lineIndex%3==1:
        # If this line is a first line in a client account
        clientNumber=splits[0].replace('\n', '')
        clientName=splits[1].replace('\n', '')

        try:
            clientAddress=splits[2].replace('\n', '')
        except:
            clientAddress=splits[1].split()
            clientAddress=clientAddress[-3]+clientAddress[-2]+clientAddress[-1].replace('\n', '')

        if line[-2].isdigit():
            creditLimit=(line[-5]+line[-4]+line[-3]+line[-2]).replace(' ', '').replace('\n', '')
        else: 
            creditLimit=""

    elif lineIndex%3==2:
        # If this line is a second line
        if len(splits)>0:
            secondAddress=splits[0].replace('\n', '')
        else:
            secondAddress=''


    elif lineIndex%3==0:
        # If this line is a third line
        city=splits[0]
        stateCode=splits[1].split()[0].replace('\n', '')
        zipCode=splits[1].split()[1].replace('\n', '')
        phoneNumber=splits[2].replace('/', '-').replace('\n', '')

        save(clientNumber, clientName, clientAddress, secondAddress, city, stateCode, zipCode, phoneNumber, creditLimit, filename)

f.close()