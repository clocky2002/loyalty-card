cardDetails = input("Welcome to the Jewelery Website. Please input your voucher code: ")

def dateCheck(): #Checks the date
    from datetime import date #import datetime protocol
    day = input('Please input the day of the month the card is valid from ') #Input day
    month = input('Please input the month of the year the card is valid from ') #Input month
    year = input('Please input the year the card is valid from ') #Input year
    expiryDate = date(year, month, day)
    today = date.today() #gets current date
    # if today is less than the expirary date
    if today < expiryDate:
        print("That is a valid date")
    else:
        print("This is an invalid date")


def voucherCode(cardDetails):
    try:
        cardDetails = int(cardDetails)
    except ValueError:
        print("That's not an int!")
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

dateCheck()
voucherCode(cardDetails)
