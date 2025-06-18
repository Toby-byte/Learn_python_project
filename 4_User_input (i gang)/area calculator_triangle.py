# we are converting our user input from string to float, 2 reasons
# 1. So we can input numbers like 9.75 in the terminal
# 2. So the can be used to calculate the area in the area variable
# otherwise we get this error: TypeError: can't multiply sequence by non-int of type 'str'
length = float(input("Input the LENGTH of the triangle: "))
width = float(input("Input the WIDTH of the triangle: "))
height = float(input("Input the HEIGHT of the triangle: "))

volume = length * width * height

print(f"The volume is {volume} cm^3")