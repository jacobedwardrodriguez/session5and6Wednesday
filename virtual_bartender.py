from random import choice
drinks = ["gin", "vodka", "whiskey", "rum", "tequila", "absinthe", "sake"]
# print(choice(drinks))
name = input("I am the virtual bartender. What is your name?")
try:
    age = input("What is your age?")
    age = int(age)
    country = input("what is your country?")
    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True

except ValueError:
    print("Dont play games with me")
else:
    if legal:
        print("Its my pleasure to serve you", choice(drinks))
    else:
        print("Dear", name, "Unfortunately I cannot serve you")


