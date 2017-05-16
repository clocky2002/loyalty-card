cardDetails = input("Please input the card number: ")

def dateCheck():  # Check the date
    import datetime  # import datetime protocol
    day = input('Please input the day the card is valid from ')  # Input day
    try:
        day = int(day)
        if True and int(day) >= 1 and int(day) <= 31:
            day = int(day)
    except ValueError:
        day = input("That was an invalid day. Please try again ")
    #########################################################################
    month = input('Please input the month the card is valid from ')
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
        month = (monthConversion[month[0:3].lower().title()])

    #############################################################################
    year = input('Please input the year the card is valid from (YYYY)')  # Input year
    ###########################################################################
    from datetime import date
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
            if cardDetails == exitCode or upper.exitCode() or lower.exitCode() or title.exitCode():
                print('You have exited the program')
                exit()
    else:
        cardDetails = input("That was an invalid code. Please try again or to exit, type end: ")
        if cardDetails == exitCode or upper.exitCode() or lower.exitCode() or title.exitCode():
            print('You have exited the program')
            exit()
        else:
            lengthCardDetails(cardDetails)

def voucherCode(cardDetails):
    digitList = [int(i) for i in str(cardDetails)]
    checkDigit = digitList.pop(7)
    digitList = digitList[::-1]
    print(digitList)
    ############################################################
    digitOne = digitList[0]
    digitOne = int(digitOne) * 2
    if int(digitOne) > 9:
        digitOne = digitOne - 9
    digitList[0] = digitOne
    print(digitList)
    #############################################################
    digitThree = digitList[2]
    digitThree = int(digitThree) * 2
    if int(digitThree) > 9:
        digitThree = digitThree - 9
    digitList[2] = digitThree
    print(digitList)
    #############################################################
    digitFive = digitList[4]
    digitFive = int(digitFive) * 2
    if int(digitFive) > 9:
        digitFive = digitFive - 9
    digitList[4] = digitFive
    print(digitList)
    #############################################################
    digitSeven = digitList[6]
    digitSeven = int(digitSeven) * 2
    if int(digitSeven) > 9:
        digitSeven = digitSeven - 9
    digitList[6] = digitSeven
    print(digitList)
    #############################################################
    digitOne = int(digitList[0])
    digitTwo = int(digitList[1])
    digitThree = int(digitList[2])
    digitFour = int(digitList[3])
    digitFive = int(digitList[4])
    digitSix = int(digitList[5])
    digitSeven = int(digitList[6])
    
    addedUp = digitOne + digitTwo + digitThree + digitFour + digitFive + digitSix + digitSeven + int(checkDigit)
    
    ## Other way to do it
    addedUp = 0;
    for number in digitList:
        addedUp += number # You int() the numbers when you added them to digitList - line 70
    #############################################################
    print(str(addedUp))
    if int(addedUp) % 10 == 0:
        print('This is a valid number')
    else:
        print("This is invalid")


dateCheck()
lengthCardDetails(cardDetails)
voucherCode(cardDetails)

