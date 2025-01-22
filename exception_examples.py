name = input("what is your name?")
print("hello", name)
age = input("How old are you ")
try:
    age = int(age) # i am trying to convert it to a number
    print("you were probably born in", 2024 - int(age))
    # new_age = age/0

except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
    # typing letters example

except ZeroDivisionError:
    print("you cant divide by zero")
    # catches when the age is divided by 0

except:
    print("something unexpected occur")

else: # this happens if no error occurred
    print("you were probably born in", 2024 - age)

finally:
    print("thanks for playing")


