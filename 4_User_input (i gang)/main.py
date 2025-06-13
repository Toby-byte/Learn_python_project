# The Input function can be used to accept input from a user
# The string inside the function displays a prompt in the terminal 

# input("Enter your name: ")

# Save the input to a variable, that can be used later in the script
# fx. in a print statement

name = input("Enter your name: ")
age = input("Enter your age: ")

# Since you can't add a integer to a string 
# We can use explicit type casting, to convert the variable age to an Integer
age = int(age) + 1

print(f"Your name is {name}") 
print(f"you are {age} years old")

# Nået til 7:00 i video'en