# Variable = A container for a value such as string, integer, float or boolean.
# variables can be assigned using '=', as shown below

# These is a string variable
# String can be thought of as a series of characters, numbers, letters and symbols...
first_name = "Tobias"
email = "Toby-byte@fake.com"
print(first_name)

# How to use an f-string, the 'f' means format...
# {} Must be used, if you want to insert a variable in your string
print(f"Hello {first_name}")
print(f"Your email is: {email}")

# These are Integeres
# Can only be whole numbers, does not have "" 
# examples
age = 25
quantity = 3

print(f"you are {age} years old")
print(f"You bought {quantity} items")

# These are Floats
# these have decimals, does not have ""
price = 25.5

print(f"the price is {price}")

# These are booleans
# Can only be True or False, the first letter must be upper-case! or they won't work!
is_student = True

print(f"Are you a student?: {is_student}")

# Here is a sneack-peck into if statements to explain booleans!


# If statements will always excute the first option, if the variable is True
# if the boolean variable is False, the command will be skipped! (Important)
if is_student:
    print("You are a student")

# If an else is added to an if statement and the boolean variable in the if statement is false
# Then the command after else will be executed 
if is_student:
    print("You are a student")
else:
    print("You are not a student")


