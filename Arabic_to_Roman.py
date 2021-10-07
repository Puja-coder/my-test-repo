import math

# Function to convert Arabic Number to Roman Numeral
def arabicToRoman(num):

    # Initializing dictonary for Integer and Roman Number Mapping(Without using Subtractive Notation)
    IntToRomanDict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "G",
        10000: "H"
    }

    # Get division of number
    l = len(str(num))
    division= pow(10, l-1)

    # Defining variable for storing Roman Number
    roman_number = ""

    while num:

        # Extracting main significant digit from number
        lastNum = int(num / division)

        # All Subtractive Notation has 4 and 9 as a significant digit like ("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), e.t.c
        # Below are the Logics for significant digit <=3, 4, 5-8 and 9.

        if lastNum <= 3:
            roman_number += (IntToRomanDict[division] * lastNum)
        elif lastNum == 4:
            roman_number += (IntToRomanDict[division] + IntToRomanDict[division * 5])
        elif 5 <= lastNum <= 8:
            roman_number += (IntToRomanDict[division * 5] + (IntToRomanDict[division] * (lastNum - 5)))
        elif lastNum == 9:
            roman_number += (IntToRomanDict[division] + IntToRomanDict[division * 10])

        # Creating next number
        num = math.floor(num % division)

        # Creating Division of Next number
        division /= 10

    return roman_number

# Driver code::
print("Example:- \n Roman Numeral of Arabic Number of 913 is: " + str(arabicToRoman(913)))

again = 'y'

while again == 'y':

    number = input("Please Enter Arabic Number to Convert into Roman Numeral: ")
    
    if int(number) <= 39999:
        print(arabicToRoman(int(number)))
    else:
        print("Please enter number less then or equal to 39999!")
        
    again = input("Would you like to test another Arabic Number (y/n): ")
    
    
# ------------------------------ End ------------------------------#