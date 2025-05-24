print("Alphabetic Telephone Number Translator")

alpha_num = input("Please enter the number you would like to translate(country code not necessary) \nPlease use XXX-XXX-XXXX format: ")

translator = ""

for char in alpha_num:
 if char.isalpha():
    if char.upper() in "ABC":
        translator += "2"
    elif char.upper() in "DEF":
        translator += "3"
    elif char.upper() in "GHI":
        translator += "4"
    elif char.upper() in "JKL":
        translator += "5"
    elif char.upper() in "MNO":
        translator += "6"
    elif char.upper() in "PQRS":
        translator += "7"
    elif char.upper() in "TUV":
        translator += "8"
    elif char.upper() in "WXYZ":
        translator += "9"
 else:
     translator += char

print(f"Here is the 10 digit translation for your number: ", translator)