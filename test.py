month = input("Enter month: ")

def ConvertMonthNameToNumber(month):
    listOfMonths = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }
    monthShort = month.strip()[:3].lower()
    try:
        monthNumber = listOfMonths[monthShort]
        return monthNumber
    except ValueError:
        print('Valid month name not found.')

convertedMonth = ConvertMonthNameToNumber(month)
