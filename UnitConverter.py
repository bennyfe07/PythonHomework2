#Unit Converter - kilometers into miles

print("Hi User, this is a unit converter tool from kilometers into miles.")

while True:
    kilometers = input("Type in kilometers, which have to be converted: ")
    kilometers = float(kilometers.replace(",","."))
    miles = kilometers * 0.621371
    print(f"{kilometers} kilometers are {miles} miles")

    decision = input("Would you like to convert another value? (y/n)")
    #.lower will also make the char lower if the user types in a Y
    if decision.lower() != "y":
        print("Thanks for using the converter!")
        break




