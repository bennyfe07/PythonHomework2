print("Welcome to the Lower Case Machine!")

while True:
    sentence = input("Type in any sentence you want in lower and upper case and I will convert it into lowercase: ")
    print(sentence.lower())

    choose = input("Would you like to convert another string? (y/n)")
    if choose.lower() != "y":
        print("Thanks for using the Lower Case Machine!")
        break
