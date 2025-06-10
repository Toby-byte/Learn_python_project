# Typecasting = The process of converting of one data type to another
# Such as Strings, integers, floats and booleans

# This can be done to ways Explicit or Implicit 

# variables we will be playing with
name = "Tobias" # String
age = 27 # Integer
gpa = 2.5 # Float
student = True # Booleans

# How to print the type of the variable, it will look something like this "<class 'class_here'>"
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# conversion methods
float() # turns variables into Floats 
int() # turns variables into Integers
str() # turns variables into Stringers

# Explicit

# Converting age (Integer) to a float, notice a comma is added!
age = float(age)

print(f"age is now a float {type(age)}")
print(age)

# Converting gpa (float) to a Integer, notice the comma is gone!
gpa = int(gpa)

print(f"gpa is now a Integer {type(gpa)}")
print(gpa)

# Converting student (boolean) to a String, it is now a series of characters!
student = str(student)

print(f"student is now a String {type(student)}")
print(student)

# when converting a value to boolean, if the value is anything but 0, the value will be True
age = bool(age)
print(age)

# If nothing is entered in a string this will also return False
age = bool("")
print(age)

# This is useful for checking a user wrote something in a field or not

# Implicit typecasting ------------------------------------------------------------------------

# Mangler boolean nået til 6:00 i videon
