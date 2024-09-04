def convert_currency():
    print("This program converts United States Dollars to Ghana Cedis")
    print()

    dollars=eval(input("enter amount in dollars: "))

    cedis=convert_to_cedis(dollars)

    print(f"That is GHc {cedis}")

convert_to_cedis= lambda dollars: dollars*15.26

convert_currency()