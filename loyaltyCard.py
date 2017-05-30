from datetime import date  # import datetime module

cardDetails = input("Please input the card number: ")

def dateCheck():
    
    validDay = False
    validMonth = False
    validYear = False
    
    day = input('Please input the day the card is valid from ')
    #Keeps asking until there is a valid day
    while (validDay == False):
        try:
            day = int(day)
            if not (day >= 1 and day <= 31):
                day = int(input("That was an invalid day. Please try again "))
            else:
                validDay = True
        except ValueError:
            day = input("That was an invalid day. Please try again ")
    #########################################################################
    month = input('Please input the month the card is valid from ')
    #Keeps asking until there is a valid month
    while validMonth == False:
        try:
            month = int(month)
        except ValueError:
            monthConversion = {
                "Jan": 1,
                "Feb": 2,
                "Mar": 3,
                "Apr": 4,
                "May": 5,
                "Jun": 6,
                "Jul": 7,
                "Aug": 8,
                "Sep": 9,
                "Oct": 10,
                "Nov": 11,
                "Dec": 12
            }
            month = monthConversion[month[0:3].lower().title()]
            
        if not (month >= 1 and month <=12):
            month = input('Please input the month the card is valid from ')
        else:
            validMonth = True

    #############################################################################
    year = input('Please input the year the card is valid from (YYYY)')  # Input year
    ###########################################################################
    today = date.today()
    card = date(int(year), int(month), int(day))
    dif = today - card
    print (dif.days)

    if (dif.days < 0):
        print ("Date cannot be in the future.")
    elif (dif.days > 365):
        print ("The card has expired.")
    elif (dif.days <= 365):
        print ("The card is valid.")
    else:
        print ("An error has occured.")

def lengthCardDetails(cardDetails):
    exitCode = ('end')
    if len(cardDetails) == 8:
        try:
            cardDetails = int(cardDetails)
        except ValueError:
            cardDetails = input("That was an invalid code. Please try again or to exit, type end: ")
            if cardDetails.lower == exitCode:
                print('You have exited the program')
                exit()
    else:
        cardDetails = input("That was an invalid code. Please try again or to exit, type end: ")
        if cardDetails.lower == exitCode:
            print('You have exited the program')
            exit()
        else:
            lengthCardDetails(cardDetails)

# Code was duplicated so made it a function
def digitChange(digit):
    digit = digit * 2
    if digit > 9:
        digit = digit - 9
    print(digit)
    return digit
    
def voucherCode(cardDetails):
    digitList = [int(i) for i in cardDetails]
    checkDigit = digitList.pop(7)
    digitList = digitList[::-1]
    print(digitList)
    ############################################################
    for i in range(0,7,2): # Starting at 0, ending at 6, iterating over every other digit
        digitList[i] = digitChange(digitList[i]) # Refering to the digitChange() defined on line 87
    #############################################################   
    addedUp = 0;
    for number in digitList:
        addedUp += number
    addedUp += checkDigit
    #############################################################
    print(str(addedUp))
    if int(addedUp) % 10 == 0:
        print('This is a valid number')
    else:
        print("This is invalid")


dateCheck()
lengthCardDetails(cardDetails)
voucherCode(cardDetails)
