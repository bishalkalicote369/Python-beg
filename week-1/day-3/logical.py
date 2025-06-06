# user_name = False
# password = True
# gmail = False
# if user_name and password:
#     print("you are singed in")
# else:
#     print("wrong password please try another passord")

user_name = False
password = True
gmail = False
if (user_name or password) and not gmail:
    print("you are singed in")
else:
    print("wrong password please try another passord")

# The not operator in Python is a unary logical operator that reverses the truth value of a condition.
is_raining = False

if not is_raining:
    print("You can go outside!")
else:
    print("Take an umbrella.")
