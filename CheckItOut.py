############################################################################# IMPORT MODULES
import datetime
from datetime import date

cardDetails = ""
dateValid = False

name = input('What is your name? ')
postCode = input('What is your postcode? ')

############################################################################# FUNCTIONS SECTION
########## Get Card Number Function
def cardNumber():
    valid = False
    while valid == False:
        try:
            cardDetails = int(input("Please input the card number: "))
            if len(str(cardDetails)) == 8:
                print ("Card number is eight digits long.")
                valid == True
                return cardDetails
            elif len(str(cardDetails)) < 8:
                print ("Card number is too short.")
            elif len(str(cardDetails)) > 8:
                print ("Card number is too long.")
            else:
                print ("An error has occured. (Card Number)")
        except ValueError:
            print ("Error. The value entered is not an integer.")

########## Check Card Date Function
def cardDate():
    def ConvertMonthNameToNumber(m):
        listOfMonths = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12
            }
        monthShort = m.strip()[:3].lower()
        if monthShort in listOfMonths:
            try:
                monthNumber = listOfMonths[monthShort]
                return monthNumber
            except ValueError:
                print('Input value error. Could not identify month.')

##### day
    valid = False
    while valid == False:
        try:
            d = int(input('Please input the day the card is valid from: '))
            if d >= 1 and d <= 31:
                valid = True
        except ValueError:
            print ("Error. Invalid entry.")
##### month
    valid = False
    while valid == False:
        m = input('Please input the number of the month the card is valid from: ')
        try:
            m = int(m)
            if m >= 1 and m <= 12:
                valid = True
        except:
            try:
                month = ConvertMonthNameToNumber(m)
                m = int(month)
                if month >= 1 and month <= 12:
                    month = int(month)
                    valid = True
            except ValueError:
                print("Input value error. Could not identify month.")

##### year
    valid = False
    while valid == False:
        try:
            y = int(input('Please input the year the card is valid from (YYYY): '))
            if (len(str(y))) == 2:
                y = int("20"+str(y))
            if y >= 2000 and y <= 2100:
                valid = True
        except ValueError:
            print ("Error. Invalid entry.")
                   
##### calculate difference in days
    today = date.today()
    card = date(y,m,d)
    dif = today - card
    if (dif.days < 0):
        print ("An error has occured.")
    elif (dif.days > 365):
        print ("An error has occured.")
    elif (dif.days <= 365):
        dateValid == True
        print ("The card is valid for "+ str(365-dif.days) + " days") #doesn't handle leap year
    else:
        print ("An error has occured.")
##### return d m and y here

########## Voucher Code Function
def voucherCode(cardNumber):
    digitList = [int(i) for i in str(cardDetails)]
    checkDigit = digitList.pop(7)
    digitList = digitList[::-1]
    ############################################################
    for i in range(0, 7, 2):  # Starting at 0, ending at 6, iterating over every other digit
        digitList[i] = digitChange(digitList[i])
    #############################################################
    addedUp = 0;
    for number in digitList:
        addedUp += number
    addedUp += checkDigit
    #############################################################
    print(str(addedUp))
    global cardValid
    if int(addedUp) % 10 == 0:
        cardValid = True 
    else:
        cardValid = False

##########Digit Change
def digitChange(digit):
    digit = digit * 2
    if digit > 9:
        digit = digit - 9
    return digit

def valid():
    if cardValid and dateValid == True:
        print('The card is valid')
    else:
        print('Card is not Valid')

############################################################################# CALL FUNCTIONS SECTION
cardNumber() #working
cardDate() # working - needs extra month validation
voucherCode(cardNumber)# working
print("Your name is: " +name)
print("Your postcode is: " +postCode)
valid()
