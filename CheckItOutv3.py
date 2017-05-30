from datetime import date  # import datetime module
from tkinter import *

window = Tk()
window.title("Check it out")
window.geometry("500x500")
#window.wm_iconbitmap('card.ico')
theLabel = Label(window, text="test")
theLabel.pack()
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
button1 = Button(bottomFrame, text="Submit")
button1.pack()


cardDetails = Entry(window, text="Please input the card number: ")


def dateCheck():
    validDay = False
    validMonth = False
    validYear = False

    ##########################################################################
    day =  Entry(window, 'Please input the day the card is valid from ')
    # Keeps asking until there is a valid day
    while (validDay == False):
        try:
            day = int(day)
            if not (day >= 1 and day <= 31):
                day = int(input("That was an invalid day. Please try again "))
            else:
                validDay = True
        except ValueError:
            day = Entry(window, "That was an invalid day. Please try again ")

    #########################################################################
    month =  Entry(window,'Please input the month the card is valid from ')
    # Keeps asking until there is a valid month
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

        if not (month >= 1 and month <= 12):
            month = Entry(window, 'Please input the month the card is valid from ')
        else:
            validMonth = True

    #############################################################################
    year = input('Please input the year the card in the valid form (YYYY)')  # Input year
    while validYear == False:
        if len(year) == 4:
            try:
                year = int(year)
                validYear = True
            except ValueError:
                year = Entry(window, 'Please input the year the card in the valid form (YYYY)')
        else:
            year =  Entry(window,'Please input the year the card in the valid form (YYYY)')

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
    validCardNumber = False
    exitCode = 'end'

    # Continues asking for a valid card number or the exit code until either is entered
    while validCardNumber == False:
        if len(cardDetails) == 8:
            try:
                cardDetails = int(cardDetails)
                validCardNumber = True
            except ValueError:
                cardDetails =  Entry(window, "That was an invalid code. Please try again or to exit, type end: ")
        elif cardDetails.lower == exitCode:
            print('You have exited the program')
            exit()


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
    for i in range(0, 7, 2):  # Starting at 0, ending at 6, iterating over every other digit
        digitList[i] = digitChange(digitList[i])
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
window.mainloop()